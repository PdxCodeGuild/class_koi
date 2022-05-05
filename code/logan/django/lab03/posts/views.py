from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .forms import LoginForm

# Create your views here.

def index(request):
    """
    This is the welcome page.
    """
    message = ""
    if request.method == "POST":
        message += "Invalid credentials.  Please try again."
    form = LoginForm()
    context = {'message': message, 'form':form}
    return render(request, "posts/index.html", context)

def world(request):
    """
    View the WORLD's chirps
    """
    context = {}
    return render(request, "posts/world.html", context)
