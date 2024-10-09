# api/management/commands/start_telegram_bot.py
from django.core.management.base import BaseCommand
from api.telegram_bot.bot import main as start_bot

class Command(BaseCommand):
    help = "Starts the Telegram bot"

    def handle(self, *args, **kwargs):
        start_bot()
