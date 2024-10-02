from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
