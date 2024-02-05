from flask import Flask, request
from telegram import Update
from telegram.ext import CommandHandler, Updater, CallbackContext

app = Flask(__name__)

# Initialize the Telegram Updater with your bot token
TOKEN = '6628499584:AAGV74jBFEELTbqFgTzfT_jMyJnKxo5zgZQ'

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define a command handler for the /start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! I am your bot.')

# Register the command handler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Define your webhook route
@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the JSON data from the request
    json_data = request.get_json()
    update = Update.de_json(json_data, updater.bot)

    # Process the update using the dispatcher
    dispatcher.process_update(update)

    return 'OK'

@app.route('/', methods=['GET'])
def index():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Cloud Usage Demo by Eyob Worku</title>
</head>
<body style="text-align: center; background-color: #f0f0f0;">

  <div style="padding: 100px;">
    <h1 style="font-size: 3em; color: #ff6600;">This web is here to demonstrate cloud usage by Eyob Worku</h1>
    <p style="font-size: 1.5em; color: #3366cc;">This is mainly an API used by Telegram bot.</p>
  </div>

</body>
</html>'''

if __name__ == '__main__':
    app.run()
    updater.start_webhook(listen='0.0.0.0', port=8443,url_path='')
    updater.bot.setWebhook(url='https://eyuman.pythonanywhere.com/')
    updater.idle()