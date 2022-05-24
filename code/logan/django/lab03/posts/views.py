from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .forms import ChirpForm
from .models import Chirp
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def index(request):
    """
    This is the welcome page.
    """
    message = ""
    if request.method == "POST":
        message += "Invalid credentials.  Please try again."
    form = AuthenticationForm
    context = {'message': message, 'form':form}
    return render(request, "posts/index.html", context)

def world(request):
    """
    View the WORLD's chirps -- NOT IN USE.
    """
    if request.method == "POST":
        # form = ChirpForm(data = request.POST)
        content = request.POST.get('content')
        Chirp.objects.create(
            content=content,
            date = timezone.now(),
            user = request.user
            )

    form = ChirpForm()
    context = {
        'form':form,
        'all_chirps': Chirp.objects.all()
    }
    return render(request, "posts/world.html", context)


def profile(request):
    """
    NOT IN USE
    """
    user = request.user
    all_chirps = Chirp.objects.all()
    context = {
        'my_chirps':all_chirps.filter(user=request.user),
        'user':user,
    }
    return render(request, "posts/profile.html", context)

def profileextend(request):
    if request.method == "POST":
        # form = ChirpForm(data = request.POST)
        content = request.POST.get('content')
        Chirp.objects.create(
            content=content,
            date = timezone.now(),
            user = request.user
            )

    form = ChirpForm()
    user = request.user
    all_chirps = Chirp.objects.all()
    context = {
        'my_chirps':all_chirps.filter(user=request.user),
        'user':user,
        'form':form
    }
    return render(request, "posts/profileextend.html", context)

def worldextend(request):
    """
    View the WORLD's chirps
    """
    if request.method == "POST":
        # form = ChirpForm(data = request.POST)
        content = request.POST.get('content')
        Chirp.objects.create(
            content=content,
            date = timezone.now(),
            user = request.user
            )

    form = ChirpForm()
    context = {
        'form':form,
        'all_chirps': Chirp.objects.all()
    }
    return render(request, "posts/worldextend.html", context)