from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Books, Authors
from django.utils import timezone


def index(request):

    books = Books.objects.all()
    authors = Authors.objects.order_by('author_name')
    if request.method == 'POST':

        name = request.POST.get('name'),
        publish_date = request.POST.get('publish_date')
        author_name = request.POST.get('author')
        author, created = Authors.objects.get_or_create(
            author_name=author_name)
        Books.objects.create(
            name=name,
            publish_date=publish_date,
            author=author,
        )
        return redirect('library:index')
    context = {
        'books': books,
        'authors': authors,
    }
    return render(request, 'library/index.html', context)


# def book(request, id: int):
#     authors = get_object_or_404(Authors, id=id)
#     books = Books.objects.all()
#     if request.method == 'POST':
#         author = request.POST.get('author')
#         name = request.POST.get('name'),
#         publish_date = request.POST.get('publish_date')
#         checked_out = request.POST.get('checked_out')
#         Books.objects.create(
#             name=name,
#             publish_date=publish_date,
#             checked_out=checked_out,
#             author=author,
#         )
#         return redirect('library:book')
#     context = {'authors': authors,
#                'books': books,
#                }
#     return render(request, 'library/book.html', context)
def checked_in(request, id):
    checked = Books.objects.get(id=id)
    checked.checked_out = True
    checked.save()
    who_checked_out_time = timezone.now
    who_checked_out = request.user.username
    Books.objects.update(
        who_checked_out=who_checked_out,
        who_checked_out_time=who_checked_out_time
    )
    print('hi')
    return redirect('library:index')
    # if request.method == 'POST':
    #     who_checked_out = request.POST.get('checkout')
    # # checked.save()

    #     return redirect('library:index')


def checked_outs(request, id):
    checked = Books.objects.get(id=id)
    checked.checked_out = False
    checked.save()
    return redirect('library:index')


# def who_checked(request, id):
#     who_check = Books.objects.get(id=id)
#     who_check.checked_out = True
#     who_check.
#     if request.method == 'POST':
#         who_checked_out_time = timezone.now()
#         who_checked_out = request.POST.get('who_checked_out')
#         Books.objects.update(
#             who_checked_out=who_checked_out,
#             who_checked_out_time=who_checked_out_time,
#         )
#         who_check.save()
#         return redirect('library:index')
