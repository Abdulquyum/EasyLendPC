# api/telegram_bot/telegram_config.py

import os

# Set your bot token and group chat ID here
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "your_token_here")
GROUP_CHAT_ID = os.getenv("GROUP_CHAT_ID", "your_group_chat_id_here")
