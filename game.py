from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ApplicationHandlerStop,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)
import os
from dotenv import load_dotenv

load_dotenv()
bot_token = os.environ.get("BOT_TOKENPOLL")


async def pre_process(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data["step"] = context.user_data.get("step", 0) + 1
    print(context.user_data, update.effective_user.full_name)
    return None


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await pre_process(update, context)
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")

async def tts_callback(update, context):
    query = update.callback_query
    bot = context.bot
    # print(query.game_short_name)
    await bot.answerCallbackQuery(query.id,url='https://tbot.xyz/lumber/')

app = ApplicationBuilder().token(bot_token).build()

app.add_handler(CommandHandler(["hello", "start"], hello))

app.add_handler(CallbackQueryHandler(tts_callback))

app.run_polling(allowed_updates=Update.ALL_TYPES)
# app.run_webhook(listen='0.0.0.0',port=443,webhook_url='https://epubpdf.onrender.com/')
