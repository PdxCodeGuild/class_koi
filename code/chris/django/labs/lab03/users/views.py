from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request):
    return render(request, 'posts/index.html')

def login_user(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('posts:home')
        else:
            message = 'login failed'
    context = {
        'message': message,
    }
    return render(request, 'users/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('posts:home')

def signup(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        message = ''
        if password != password1:
            message += 'Passwords do not match. '
        if User.objects.filter(username=username).exists():
            message += 'Username already exists. '
        if message:
            message += 'Please try again.'
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('posts:home')
        context = {'message': message,}
    return render(request, 'users/signup.html', context)
