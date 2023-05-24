from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth

# Create your views here.

def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    if request.method == "POST":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        message = request.POST['sms']
        Contact(
                contact_name = firstName,
                contact_surname = lastName,
                contact_email = email,
                contact_message = message
            ).save()
        messages.success(request, 'Message sent!')
    return render(request, 'contactus.html')

def iphone6(request):
    return render(request, 'iphone6.html')

def iphone6plus(request):
    return render(request, 'iphone6plus.html')

def iphone14promax(request):
    return render(request, 'iphone14promax.html')

def se1100(request):
    return render(request, 'se1100.html')

def sga12(request):
    return render(request, 'sga12.html')

def sgs22ultra(request):
    return render(request, 'sgs22ultra.html')

def iphone11(request):
    return render(request, 'iphone11.html')

def iphone12(request):
    return render(request, 'iphone12.html')

def iphone13(request):
    return render(request, 'iphone13.html')

def sgs6(request):
    return render(request, 'sgs6.html')

def sgs6e(request):
    return render(request, 'sgs6e.html')

def sgs6ep(request):
    return render(request, 'sgs6ep.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'register.html', context)

def login(request):
    if request.method == "POST":
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')