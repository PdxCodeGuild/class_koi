from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def login_user(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('groceries:home')
        else:
            context = {'message': 'Incorrect username or password.  Please try again.'}

    return render(request, 'users/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('groceries:home')

def signup(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        message = ''
        if password1 != password2: # the passwords don't match
            message += 'Passwords do not match.  '
        if User.objects.filter(username=username).exists(): # the username is already taken
            message += 'Username already taken.  '
        if message: # this will run if there are any characters in the message string
            message += 'Please try again.'
        else:
            user = User.objects.create_user(username=username, password=password1)
            login(request, user)
            return redirect('groceries:home')
        context = {'message': message}
    return render(request, 'users/signup.html', context)