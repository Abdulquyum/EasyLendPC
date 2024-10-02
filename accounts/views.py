from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="accounts:login")
def dashboard(user_request):
    return render(user_request, "dashboard.html")


def login_view(user_request):
    if user_request.method == "POST":
        username = user_request.POST["username"]
        password = user_request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        # check if user is availble in the database
        if user is not None:
            auth.login(user_request, user)
            return redirect("accounts:dashboard")
        else:
            messages.info(user_request, "Invalid username or password")
            return redirect("accounts:login")
    return render(user_request, "login.html")


def signup_view(user_request):
    # Collect user data
    if user_request.method == "POST":
        email = user_request.POST["email"]
        username = user_request.POST["username"]
        password = user_request.POST["password"]
        password2 = user_request.POST["password2"]

        if password == password2:
            # Check if user already exist
            if User.objects.filter(email=email).exists():
                messages.info(user_request, "Email taken")
                return redirect("accounts:signup")
            elif User.objects.filter(username=username).exists():
                messages.info(user_request, "Username taken")
                return redirect("accounts:signup")
            else:  # Create a new user if it dosen't exist
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()

                # Log user in
                user_login = auth.authenticate(username=username, password=password)
                auth.login(user_request, user_login)
                return redirect("accounts:dashboard")

        else:
            messages.info(user_request, "Input Matching Passwords")
            return redirect("accounts:signup")
    else:
        return render(user_request, "signup.html")


@login_required(login_url="login")
# log the user out
def logout_view(user_request):
    auth.logout(user_request)
    return redirect("accounts:login")
