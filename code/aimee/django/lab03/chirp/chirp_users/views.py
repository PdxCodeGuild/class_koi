from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# from .models import SignUp, LogIn
from .forms import NewUserForm

# CHIRP USERS ------------------------- #

def index(request):
    ...
    return render(request, 'chirp_users/index.html',)

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # automatically logs user in if registration works
            messages.success(request, 'You\'ve registered successfully!')
            return redirect('chirp_users:index') # send user back to homepage if login works
        messages.error(request, 'Oops! Registration didn\'t work - maybe you missed something!')
    form = NewUserForm()
    return render(request=request, template_name="chirp_users/register.html", context={'register_form':form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None: # if user is registered
                login(request, user) # log user in
                messages.info(request, f'You\'re logged in, {username}!')   
                return redirect('chirp_users:index')
            else:
                messages.error(request,'Hmm, either your username or password is invalid!')
        else:
            messages.error(request,'Hmm, either your username or password is invalid!')
    form = AuthenticationForm()
    return render(request=request, template_name="chirp_users/login.html", context={'login_form':form})

def logout_request(request):
    logout(request)
    messages.info(request, 'You\'ve been logged out!')
    return redirect('chirp_users:index')