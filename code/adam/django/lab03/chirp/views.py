from django.shortcuts import render, redirect
from django.utils import timezone

from .models import ChirpPost

def index(request):
    posts = ChirpPost.objects.all()
    if request.method == 'POST':
        author = request.POST.get('author')
        post_text = request.POST.get('message')
        date_posted = timezone.now()
        if post_text == '':
            ...
        else :
            ChirpPost.objects.create(
                author=author,
                post_text=post_text,
                date_posted=date_posted,
                user=request.user
        )

        return redirect('posts:home')

    context = {
        'message' : 'Chirpity Chirp Chirp, this is home, chirpy',
        'posts' : posts
    }
    return render(request, 'chirp/index.html', context)

def detail(request, id: int):
    post = ChirpPost.objects.get(id=id)
    # print(posts.author)
    context = {
        'post' : post
    }
    return render(request, 'chirp/detail.html', context)

