from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from db_con import MongoManager
import os

db_url = os.environ.get('MONGO_URL')
conn = MongoManager(db_url)
conn.connect()

if conn.is_connected:
    print("Mongo DB connected...")
else:
    print("Mongo DB was not connected...")

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def eyu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update)
    await update.message.reply_text(f'Hello {update.effective_user.username}')

app = ApplicationBuilder().token("6628499584:AAGV74jBFEELTbqFgTzfT_jMyJnKxo5zgZQ").build()

app.add_handler(CommandHandler("hello", hello))

app.add_handler(CommandHandler("eyu", eyu))

# app.run_polling(allowed_updates=Update.ALL_TYPES)
app.run_webhook(
    listen='0.0.0.0',
    port=443,
    webhook_url='https://pptbot.onrender.com/'
)