from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ApplicationHandlerStop,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
from clod import convertPdf, getMe
import os
from dotenv import load_dotenv
import json

load_dotenv()
bot_token = os.environ.get("BOT_TOKEN")


async def pre_process(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data["step"] = context.user_data.get("step", 0) + 1
    print(context.user_data, update.effective_user.full_name)
    return None


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await pre_process(update, context)
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")


async def getUser(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    usename, points = getMe()
    await update.message.reply_text(f"{usename}\n{points}")


async def linkConv(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    link = update.message.text.split()
    if len(link) == 2:
        f_name = link[1].split('?')[0].split('/')[-1].split('.')[0]+'.pdf'
        # print(f_name)
        conUrl = convertPdf(link[1], f_name)
        await update.message.from_user.send_document(document=conUrl)


async def pdfDow(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    link = update.message.text.split()
    if len(link) == 2:
        await update.message.from_user.send_document(document=link[1])


async def eyu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await pre_process(update, context)
    await update.message.reply_text(f"Hello {update.effective_user.username}")


async def myFile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file_name = update.message.document.file_name.split('.')[0] + '.pdf'
    # file_id = update.message.document.file_id
    new_file = await update.message.document.get_file()
    conUrl = convertPdf(new_file.file_path, file_name)
    await update.message.from_user.send_document(document=conUrl)
    await update.message.reply_text(f"Your file converted {update.effective_user.username}")


app = ApplicationBuilder().token(bot_token).build()

# app.add_handler(MessageHandler(None, pre_process))

app.add_handler(CommandHandler(["hello", "start"], hello))

app.add_handler(CommandHandler("getme", getUser))

app.add_handler(CommandHandler("link", linkConv))

app.add_handler(CommandHandler("pdf", pdfDow))

app.add_handler(MessageHandler(filters.Document.ALL, myFile))

app.add_handler(CommandHandler("eyu", eyu))

# app.run_polling(allowed_updates=Update.ALL_TYPES)
app.run_webhook(listen='0.0.0.0', port=443,
                webhook_url='https://epubpdf.onrender.com/')
