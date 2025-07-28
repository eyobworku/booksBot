from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    ApplicationBuilder,
    ApplicationHandlerStop,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
from clod import convertPdf, getMe, mergeFiles
import os
from dotenv import load_dotenv
import json

load_dotenv()
bot_token = os.environ.get("BOT_TOKEN")

MERGING = range(2)


# async def pre_process(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     context.user_data["step"] = context.user_data.get("step", 0) + 1
#     print(context.user_data, update.effective_user.full_name)
#     return None


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # await pre_process(update, context)
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")


# ====== MERGE HANDLERS ======


async def merge(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["merge_files"] = []
    await update.message.reply_text(
        "Please send PDF files one by one. When you're done, press 'Done'.",
        reply_markup=ReplyKeyboardMarkup(
            [["Done"]], one_time_keyboard=True, resize_keyboard=True
        ),
    )
    return MERGING


async def collect_files(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    document = update.message.document
    if not document:
        await update.message.reply_text("Please send a valid file.")
        return MERGING

    file_name = document.file_name or "file.pdf"
    new_file = await document.get_file()
    print(new_file.file_path)
    context.user_data["merge_files"].append(new_file.file_path)
    await update.message.reply_text(f"Added: {file_name}")
    return MERGING

async def set_merged_filename(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # when you get a text set it as a file name in context
    file_name = update.message.text.strip() + ".pdf" or "merged_file.pdf"
    context.user_data["merged_filename"] = file_name
    await update.message.reply_text(f"Set merged file name to: {file_name}")
    return MERGING

async def done_merging(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    urls = context.user_data.get("merge_files", [])
    file_name = context.user_data.get("merged_filename", "merged_file.pdf")
    if len(urls) < 2:
        await update.message.reply_text("Need at least 2 files to merge.")
        return MERGING

    try:
        file_url = mergeFiles(urls,file_name)
        
        await update.message.reply_text("Here is your merged file:")
        await update.message.from_user.send_document(document=file_url)
    except Exception as e:
        print("Merge error:", e)
        await update.message.reply_text("Merging failed. Please try again later.")

    context.user_data.pop("merge_files", None)
    await update.message.reply_text(
        "Merge complete.", reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data.pop("merge_files", None)
    await update.message.reply_text(
        "Merge canceled.", reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


async def getUser(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username, points = getMe()
    print(f"Username: {username}, Points: {points}")
    await update.message.reply_text(f"The remaining points are {points}")


async def linkConv(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    link = update.message.text.split()
    if len(link) == 2:
        f_name = link[1].split("?")[0].split("/")[-1].split(".")[0] + ".pdf"
        # print(f_name)
        bol, conUrl = convertPdf(link[1], f_name)
        if not bol:
            await update.message.reply_text(
                "Conversion failed. The api we using is free and has some limitations. Please try again the next day."
            )
            return
        await update.message.from_user.send_document(document=conUrl)


async def pdfDow(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    link = update.message.text.split()
    if len(link) == 2:
        await update.message.from_user.send_document(document=link[1])


async def myFile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file_name = update.message.document.file_name.split(".")[0] + ".pdf"
    # file_id = update.message.document.file_id
    new_file = await update.message.document.get_file()
    bol, conUrl = convertPdf(new_file.file_path, file_name)
    if not bol:
        await update.message.reply_text(
            "Conversion failed. The api we using is free and has some limitations. Please try again the next day."
        )
        return
    await update.message.from_user.send_document(document=conUrl)
    await update.message.reply_text(
        f"Your file converted {update.effective_user.username}"
    )


app = ApplicationBuilder().token(bot_token).build()

# app.add_handler(MessageHandler(None, pre_process))

app.add_handler(CommandHandler(["hello", "start"], hello))

app.add_handler(CommandHandler("getme", getUser))

app.add_handler(CommandHandler("link", linkConv))

app.add_handler(CommandHandler("pdf", pdfDow))

merge_conv = ConversationHandler(
    entry_points=[CommandHandler("merge", merge)],
    states={
        MERGING: [
            MessageHandler(filters.Document.ALL, collect_files),
            MessageHandler(filters.TEXT & filters.Regex("^Done$"), done_merging),
            MessageHandler(filters.TEXT & ~filters.Regex("^Done$"), set_merged_filename),
        ]
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)
app.add_handler(merge_conv)
app.add_handler(MessageHandler(filters.Document.ALL, myFile))


# app.run_polling(allowed_updates=Update.ALL_TYPES)
app.run_webhook(listen='0.0.0.0', port=443,
                webhook_url='https://epubpdf.onrender.com/') #replace with your link
