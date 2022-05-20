from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Books, Authors, Checked_Book
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


def book(request, id: int):
    books = Books.objects.filter(id=id)
    checked = Checked_Book.objects.filter(name_id=id)
    context = {
        'books': books,
        'checked': checked
    }

    return render(request, 'library/book.html', context)


def checked_in(request, id):
<<<<<<< Updated upstream
    checked = Books.objects.get(id=id)
    checked.checked_out = False
    checked.save()
    # if request.method == 'POST':
    #     who_checked_out = request.POST.get('checkout')
    # # checked.save()

    #     return redirect('library:index')


def checked_outs(request, id):
    checked = Books.objects.get(id=id)
    checked.checked_out = True
    checked.who_checked_out_time = timezone.now
    checked.who_checked_out = request.user.username
    checked.save()

    print('hi')
=======
    name = Books.objects.get(id=id)
    name.checked_out = False
    name.save()
    who_checked_in = request.user.username
    Checked_Book.objects.create(
        name=name,
        checked_out=False,
        who_checked_in_time=timezone.now(),
        who_checked_in=who_checked_in
    )
    print('hi')
    return redirect('library:index')


def checked_outs(request, id):
    name = Books.objects.get(id=id)
    name.checked_out = True
    name.save()
    who_checked_out = request.user.username
    Checked_Book.objects.create(
        name=name,
        checked_out=True,
        who_checked_out_time=timezone.now(),
        who_checked_out=who_checked_out


    )
    print('hello')
>>>>>>> Stashed changes
    return redirect('library:index')
