from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import PostsForm
from .models import Posts

def index(request):
    if request.method == 'POST':
        # I need to get the users info to save into the form.
        form = PostsForm(request.POST)
        print(form)
        if form.is_valid():
            chirp = form.save(commit=False)
            chirp.author = request.user
            chirp.date_written = datetime.now()
            chirp.save()
            return redirect('posts:home')
        else:
            message = 'Invalid Fields Provided.'
    form = PostsForm()
    print(form)
        
    posts = Posts.objects.all()
    context = {
        'posts': posts,
        'form': form,
    }
    return render(request, 'posts/index.html', context)

def profile(request, author:str):
    author = User.objects.get(username=author)
    context = {
        'author': author,
    }
    return render(request, 'posts/profile.html', context)
    
# def chirp(request):
    # if request.method == 'POST':
    #     form = PostsForm(request.POST)
    #     print(form)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('posts:chirp')
