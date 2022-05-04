from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


from .models import Post
from .forms import PostForm

# POSTS
@ login_required
def post_request(request):
    user = request.user
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.username = user
            data.save()
            messages.success(request, 'Your chirp posted successfully!')
            return redirect('chirp_users:index')
    else:
        form = PostForm()
    return render(request, 'chirp_posts/post.html', {'post_form':form})
           





# return render(request=request, template_name="chirp_posts/post.html", context={'post_form':form})  