# api/telegram_bot/bot.py
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

load_dotenv()

# TOKEN = os.getenv("TELEGRAM_TOKEN", "7926189230:AAFcdMleY25JBfrdRIxvpf9EGDBFQiM-l6A")  # Replace with your token or use .env
TOKEN = '7926189230:AAFcdMleY25JBfrdRIxvpf9EGDBFQiM-l6A'
GROUP_CHAT_ID = '4583362385'

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to EasyLendPC Bot! How can I help you today?")

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Here are some commands you can use: /start, /help")

def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    update.message.reply_text(f"You said: {user_message}")

    # Print Chat ID
    chat_id = update.message.chat.id
    print(f"Chat ID: {chat_id}")

def forward_message(update: Update, context: CallbackContext):
    GROUP_CHAT_ID = "your_group_chat_id_here"  # Replace with your actual group chat ID
    context.bot.send_message(chat_id=GROUP_CHAT_ID, text=update.message.text)


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_message))  # Add this line

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
