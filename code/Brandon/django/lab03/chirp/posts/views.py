from django.shortcuts import render

import datetime

from django.http import HttpResponse
from .models import Posts


def index(request):
    posts = Posts.objects.all()
    if request.method == 'POST':
        post = request.POST.get('post')
        posted_time = datetime.datetime.now()
    return render(request, 'posts/index.html')
