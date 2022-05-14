from django.shortcuts import render
from .models import Chirp
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = {'chirps': Chirp.objects.all}
    return render(request, 'posts/index.html', context)