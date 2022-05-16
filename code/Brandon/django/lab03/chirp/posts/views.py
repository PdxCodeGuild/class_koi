from django.shortcuts import redirect, render
from .models import Posts, Users


from django.http import HttpResponse
from django.utils import timezone


def index(request):
    posts = Posts.objects.all()
    authors = Users.objects.all()
    if request.method == 'POST':
        print('hello')
        posted_message = request.POST.get('posted_message')
        posted_time = timezone.now().replace(microsecond=0)
        user_name = request.user.username
        author, created = Users.objects.get_or_create(
            user_name=user_name)
        Posts.objects.create(
            posted_message=posted_message,
            posted_time=posted_time,
            author=author
        )
        return redirect('posts:index')
    context = {
        'posts': posts,
        'authors': authors
    }
    return render(request, 'posts/index.html', context)


def user_page(request):

    posts = Posts.objects.all()
    authors = Users.objects.all()
    context = {
        'posts': posts,
        'authors': authors
    }

    return render(request, '<int:id>/account.html', context)
