from telegram import Update
from telegram.ext import ApplicationBuilder,ApplicationHandlerStop, CommandHandler, ContextTypes,ConversationHandler,MessageHandler,filters
import os
from dotenv import load_dotenv
load_dotenv()
bot_token = os.environ.get('BOT_TOKEN')

async def pre_process(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data["step"] = context.user_data.get("step", 0) + 1
    print(context.user_data,update.effective_user.full_name)    
    return None

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await pre_process(update,context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def eyu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await pre_process(update,context)
    await update.message.reply_text(f'Hello {update.effective_user.username}')

app = ApplicationBuilder().token(bot_token).build()

# app.add_handler(MessageHandler(None, pre_process))

app.add_handler(CommandHandler(["hello",'start'], hello))

app.add_handler(CommandHandler("eyu", eyu))

app.run_polling(allowed_updates=Update.ALL_TYPES)
# app.run_webhook(listen='0.0.0.0',port=443,webhook_url='https://pptbot.onrender.com/')