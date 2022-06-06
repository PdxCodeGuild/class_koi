from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.models import User

from .models import ChirpPost

def index(request):
    posts = ChirpPost.objects.all().order_by('-date_posted')
    if request.method == 'POST':
        post_text = request.POST.get('message')
        date_posted = timezone.now()
        ChirpPost.objects.create(
            post_text=post_text,
            date_posted=date_posted,
            author=request.user
    )

        return redirect('posts:home')

    context = {
        'message' : 'Chirpity Chirp Chirp, this is home, chirpy',
        'posts' : posts
    }
    return render(request, 'chirp/index.html', context)

def detail(request, id: int):
    author = User.objects.get(id=id)
    posts = author.chirps.all().order_by('-date_posted')
    # print(posts.author)
    context = {
        'author' : author,
        'posts' : posts,
    }
    return render(request, 'chirp/detail.html', context)

# def toggle_date_posted(request):
    



