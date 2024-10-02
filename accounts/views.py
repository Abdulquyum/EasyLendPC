from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm

# Create your views here.


@login_required(login_url="/accounts/login")
def dashboard(request):
    return render(request, "dashboard.html")


def signup_view(request):

    return render(request, "signup.html")


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome Back {username}")
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid Form Submission")
    else:
        form = UserLoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    return render(request, "logout.html")
