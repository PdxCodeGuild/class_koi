from django.http import HttpRequest
from django.shortcuts import render


def login_user(request):
    return render(request, 'users/login.html')

def logout_user(request):
    return render(request, 'chirp/index.html')

def signup(request):
    return render(request, 'users/signup.html')

