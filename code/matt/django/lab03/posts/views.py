from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Post
from .forms import PostForm


new_post_form = PostForm()

def index(request):
    posts = get_list_or_404(Post)
    context = {
        'posts': posts,
        'new_post_form': new_post_form,
    }
    return render(request, 'posts/index.html', context)

def user_feed(request, author):
    author = get_object_or_404(User, username=author)
    posts = get_list_or_404(Post, author=author)
    context = {
        'posts': posts,
        'new_post_form': new_post_form,
    }
    return render(request, 'posts/index.html', context)

def add_post(request):
    if request.method == 'POST':
        author = request.user
        text_content = request.POST.get('text_content')
        image_content = request.FILES.get('image_content')
        timestamp = timezone.now()
        Post.objects.create(
            author=author,
            text_content=text_content,
            image_content=image_content,
            timestamp=timestamp,
        )
        this_post = get_object_or_404(Post, author=request.user, timestamp=timestamp)
        return redirect('posts:post_detail', author=request.user, id=this_post.id)
    context = {
        'new_post_form': new_post_form,
    }
    return render(request, 'posts/new.html', context)

def post_detail(request, id, author):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
        'new_post_form': new_post_form,
    }
    return render(request, 'posts/post_detail.html', context)

def edit_post(request, id, author):
    ...

def delete_post(request, id, author):
    ...