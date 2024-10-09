#!/usr/bin/env python3

from django.shortcuts import render
from django.http import JsonResponse
from telegram import Update
from telegram.ext import Dispatcher
from django.http import JsonResponse
import json
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView #list laptops and present its description
from .models import Laptop, LendOutPc
from django.urls import reverse_lazy
from django.shortcuts import redirect


# Create bot instance with your token
# bot = Bot(token="7926189230:AAFcdMleY25JBfrdRIxvpf9EGDBFQiM-l6A")

# def start(update, context):
#     update.message.reply_text("Hello! Let's chat and negotiate.")

# def handle_message(update, context):
#     message = update.message.text
#     # Handle user input and send messages
#     update.message.reply_text(f"You said: {message}")

# # Initialize and start bot
# def run_bot():
#     updater = Updater("7926189230:AAFcdMleY25JBfrdRIxvpf9EGDBFQiM-l6A", use_context=True)
#     dp = updater.dispatcher
#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(MessageHandler(Filters.text, handle_message))
#     updater.start_polling()
#     updater.idle()

# #  webhoook to send real time data from telegram to app
# def telegram_bot_webhook(request):
#     if request.method == 'POST':
#         # Parse the incoming request from Telegram
#         request_data = json.loads(request.body.decode('utf-8'))

#         # Extract message or command sent by the user
#         message = request_data.get('message', {}).get('text', '')

#         # Respond to the user based on the message
#         # You can add more logic here to handle different commands or messages
#         if message == '/start':
#             response_message = 'Welcome to EasyLendPC! How can I assist you today?'
#         else:
#             response_message = 'Thank you for your message!'

#         # Send response back to Telegram (or handle any bot actions here)
#         return JsonResponse({'message': response_message})
    
#     return JsonResponse({'error': 'Invalid request method'}, status=400)

def telegram_bot_webhook(request):
    return redirect("https://t.me/easylendpc_bot")

def home(request):
    # Home page or LAnding page
    return render(request, 'home.html', {})

class DisplayLaptop(ListView):
    # list every available laptops to te display page
    model = Laptop
    template_name = 'display.html'

class LaptopDetails(DetailView):
    #Give details of individual laptops when clicked
    model = Laptop
    template_name = 'laptop_details.html'

class AddLaptop(CreateView):
    # add laptop and details available for lend
    model = Laptop
    template_name = 'add_laptop.html'
    fields = '__all__'

class UpdateLaptop(UpdateView):
    # Edit and update laptop details available for lend
    model = Laptop
    template_name = 'update_laptop.html'
    fields = ['laptop_name', 'description', 'status']

class DeleteLaptop(DeleteView):
    # Delete laptop from from DB
    model = Laptop
    template_name = 'delete_laptop.html'
    success_url = reverse_lazy('display')

class UserAddLaptop(CreateView):
    # User and laptop and details available for lend
    model = LendOutPc
    template_name = 'userToLend.html'
    fields = '__all__'

class UserDisplayLaptop(ListView):
    # list every available laptops to te display page
    model = LendOutPc
    template_name = 'nonCompanyPc.html'


class UserLaptopDetails(DetailView):
    #Give details of individual laptops when clicked
    model = LendOutPc
    template_name = 'non_company_details.html'







