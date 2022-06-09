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
            return redirect('posts:index')
        else:
            context = {'message': 'Incorrect username or password.  Please try again.'}

    return render(request, 'users/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('posts:index')

def register_user(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        message = ''
        if User.objects.filter(username=username).exists():
            message += 'Username already taken. Please try again.'
        elif password1 != password2:
            message += 'Passwords do not match. Please try again.'
        if not message:
            user = User.objects.create_user(username=username, password=password1)
            login(request, user)
            return redirect('posts:index')
        context = {'message': message}
    return render(request, 'users/register.html', context)