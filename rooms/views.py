from django.db import models
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages


def index(request):
    return render(request, "home.html")


def login(request):
    return render(request, "login.html")


def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass']
        user = authenticate(username=username, password=pass1)
        if user is not None:
            auth_login(request, user)
            # print(user.actype)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials, Try again")
            return redirect('login')
    else:
        messages.error(request, "Login First!")
        return redirect('login')


def signup(request):
    return render(request, "signup.html")


def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        actype = request.POST['ac-type']
        pass1 = request.POST['pass']
        pass2 = request.POST['pass2']
        contact = request.POST['contact']
        add = request.POST['add']

        # check for inputs
        if not username.islower():
            messages.error(
                request, "Username should only be in lower case")
            return redirect('signup')
        if len(username) > 10:
            messages.error(
                request, "Username should only contain 10 characters")
            return redirect('signup')
        if not username.isalnum():
            messages.error(
                request, "Username should only contain letters and numbers")
            return redirect('signup')
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('signup')
        # add user to models
        myuser = User.objects.create_user(username, email, pass1)
        myuser.name = name
        myuser.contact = contact
        myuser.add = add
        myuser.actype = actype
        myuser.save()

        # redirect user to homepage
        messages.success(
            request, "Your Book It account has been created, Login to continue")
        return redirect('login')
    else:
        messages.error(request, "Signup First!")
        return redirect('signup')


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged out")
    return redirect("home")


def rooms(request):
    return render(request, "user/view-rooms.html")
