from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.core.paginator import Paginator


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
           
class PostView(ListView):
    model = Post
    template_name = 'chirp_users/index.html'
    ordering = ['-post_date']
    # paginate_by = 10
    context_object_name = 'posts'
    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        return context

class ProfileView(ListView):
    model = Post
    template_name = 'chirp_posts/profile.html'
    context_object_name = 'posts'
    # paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return context
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(username=user).order_by('-post_date')






# return render(request=request, template_name="chirp_posts/post.html", context={'post_form':form})  