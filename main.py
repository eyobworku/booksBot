from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("6628499584:AAGV74jBFEELTbqFgTzfT_jMyJnKxo5zgZQ").build()

app.add_handler(CommandHandler("hello", hello))

# app.run_polling(allowed_updates=Update.ALL_TYPES)
app.run_webhook(
    listen='0.0.0.0',
    port=443,
    webhook_url='https://pptbot.onrender.com/'
)