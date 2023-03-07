import logging
import Responses
from telegram.ext import *
import Constants as keys


# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')

print("Bot started...")

def start_command(update, context):
    update.message.reply_text('Hello there! Type a Movie or a TV Show you\'d like to request!')


def help_command(update, context):
    update.message.reply_text('If you need help! You should message Kay: @Linashakrabina')

def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')
    response = Responses.get_response(text)
    #Bot response
    update.message.reply_text(response)



def error(update, context):
    print(f"Update {update} caused error {context.error}")


# Run the programme
def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(2.0)
    updater.idle()


main()















