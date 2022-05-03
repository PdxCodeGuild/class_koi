
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.utils import timezone

from .models import Author, Book, Checkout

def index(request: HttpRequest):
    authors = Author.objects.all()
    books = Book.objects.all()
    context = {
        'authors': authors,
        'books': books,
        'message': 'Library Central',
    }
    return render(request, 'library_app/index.html', context)

def detail(request, id: int):
    print(id)
    book = Book.objects.get(id=id)
    context = {
        'book': book
    }
    return render (request, 'library_app/detail.html', context)

def checkout(request, id):
    book = Book.objects.get(id=id)
    # checkout = Checkout.objects.get(id=id)
    Checkout.objects.create(
        book = book,
        checked_out_by = request.POST.get('name'),
        checked_out_date = timezone.now()
    )
    book.checked_out = True
    book.save()
    return redirect(f'/library_app/{book.id}')

def checkin(request, id):
    book = Book.objects.get(id=id)
    checkouts = book.checkouts.all()
    last_checkout = checkouts.last()
    last_checkout.checked_in_date = timezone.now()
    last_checkout.save()
    book.checked_out = False
    book.save()
    return redirect(f'/library_app/{book.id}')
