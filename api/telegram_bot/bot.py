import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

load_dotenv()

TOKEN = '7926189230:AAFcdMleY25JBfrdRIxvpf9EGDBFQiM-l6A'  # Use your token from .env or directly
GROUP_CHAT_ID = '-4583362385'  # Ensure this is the correct group chat ID
user_dict = {}  # Dictionary to store user messages and IDs

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to EasyLendPC Bot! How can I help you today?")

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Here are some commands you can use: /start, /help")

def forward_message(update: Update, context: CallbackContext):
    # Forward the user's message to the group chat ID
    user_message = update.message.text
    user_id = update.message.chat_id  # Use chat_id instead of chat.id
    message_id = str(update.message.message_id)

    # Store in user_dict for potential reply handling
    user_dict[message_id] = user_id  # Store message ID as key and user ID as value
    
    # Prepare message reference
    msg_reference = f"RefID: {user_id}"

    # Forward the message to the group
    context.bot.send_message(chat_id=GROUP_CHAT_ID, text=f"{msg_reference} | {user_message}")
    update.message.reply_text("Welcome to EasyLendPC Bot!\nThe admin will get back to you shortly")

   

def group_reply_handler(update: Update, context: CallbackContext):
    group_message = update.message.text

    if "RefID:" in group_message:
        # Extract user ID from RefID
        ref_id = group_message.split("RefID:")[1].strip().split(" ")[0]

        # Send the reply back to the user
        reply_message = f"Reply from group: {group_message}"
        context.bot.send_message(chat_id=ref_id, text=reply_message)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_message))
    dp.add_handler(MessageHandler(Filters.chat(int(GROUP_CHAT_ID)) & Filters.text, group_reply_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
