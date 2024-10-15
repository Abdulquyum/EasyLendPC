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


def telegram_bot_webhook(request):
    return redirect("https://t.me/easylendpc_bot")

def home(request):
    # Home page or LAnding page
    return render(request, 'home.html', {})

class DisplayLaptop(ListView):
    # list every available laptops to te display page
    model = Laptop
    template_name = 'display.html'
    ordering = ['-id']

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
    fields = ['name', 'description', 'status']

class DeleteLaptop(DeleteView):
    # Delete laptop from from DB
    model = Laptop
    template_name = 'delete_laptop.html'
    context_object_name = 'laptop'
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
    ordering = ['-id']


class UserLaptopDetails(DetailView):
    #Give details of individual laptops when clicked
    model = LendOutPc
    template_name = 'non_company_details.html'
    context_object_name = 'userpc'

class UserUpdateLaptop(UpdateView):
    # Edit and update laptop details available for lend
    model = LendOutPc
    template_name = 'update_userLaptop.html'
    fields = ['pc_name', 'pc_description', 'pc_status', 'phone_number']

class UserDeleteLaptop(DeleteView):
    # Delete laptop from from DB
    model = LendOutPc
    template_name = 'delete_userLaptop.html'
    context_object_name = 'userpc'
    success_url = reverse_lazy('display')

def administration(request):
    # Administration page
    return render(request, 'administration.html')

def about(request):
    # About us page
    return render(request, 'about_us.html')
