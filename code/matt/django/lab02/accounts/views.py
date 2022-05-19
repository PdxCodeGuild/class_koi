from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from time import sleep

# from .models import 

# def index(request):
#     context = {
#         'message': 'blaahhhhhh',
#     }
#     return render(request, 'accounts/index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('library:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def success(request):
    ...
    sleep(5)
    return redirect('library:index')

def profile(request):
    ...