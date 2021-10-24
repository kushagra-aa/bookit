from django.http.response import Http404
from . import models
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .models import Room


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
            return redirect('rooms:home')
        else:
            messages.error(request, "Invalid credentials, Try again")
            return redirect('rooms:login')
    else:
        messages.error(request, "Login First!")
        return redirect('rooms:login')


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
        return redirect('rooms:login')
    else:
        messages.error(request, "Signup First!")
        return redirect('rooms:signup')


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged out")
    return redirect("rooms:home")


def rooms(request):
    allrooms = Room.objects.all()
    forFrontend = {
        'rooms': allrooms
    }
    return render(request, "user/view-rooms.html", forFrontend)


def room(request, room_id):
    try:
        room = Room.objects.get(pk=room_id)
    except:
        raise Http404("Room Id Is Invalid!")
    return render(request, "user/room.html", {'room': room})


def seller(request):
    return render(request, "seller/seller.html")


def addRoom(request):
    return render(request, "seller/add-room.html")


def handleRoom(request):

    if request.method == 'POST':
        size = request.POST['room_size']
        image = request.POST['image']
        address = request.POST['address']
        city = request.POST['city']
        rate = request.POST['rate']
        floor = request.POST['floor']
        furnishing = request.POST['furnishing']
        area = request.POST['area']
        parking = request.POST['parking']
        description = request.POST['description']

        # check for inputs

        # add user to models
        newroom = models.Room.objects.create()
        newroom.image = image
        newroom.room_size = size
        newroom.address = address
        newroom.city = city
        newroom.rate = rate
        newroom.floor = floor
        newroom.furnishing = furnishing
        newroom.area = area
        newroom.parking = parking
        newroom.description = description
        newroom.seller_id = str(request.user)
        newroom.save()

        # redirect user to homepage
        messages.success(
            request, "Your Palce Have Been Successfully added")
        return redirect('rooms:home')
    else:
        messages.error(request, "Signin First!")
        return redirect('rooms:home')
