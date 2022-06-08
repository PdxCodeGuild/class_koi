from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from datetime import datetime

from .models import Book, CheckOut

def index(request: HttpRequest):

    books = Book.objects.all()
    checkouts = CheckOut.objects.all()
    print(checkouts)
    context = {
        'books': books,
        'checkouts': checkouts,
    }

    return render(request, 'library/index.html', context)

def detail(request: HttpRequest, id: int):
    print(id)
    book = Book.objects.get(id=id)
    checkouts = CheckOut.objects.filter(book=book)
    context = {
        'book': book,
        'checkouts': checkouts,
    }
    return render(request, 'library/detail.html', context)

def check_out(request: HttpRequest, id):
    reader = request.POST.get('reader')
    print(reader)
    book = Book.objects.get(id=id)
    book.checked_out = True
    book.save()
    
    checkout = CheckOut.objects.create(book=book, reader=reader, date_checked_out=datetime.now())
    print(checkout)
    

    return redirect('/library')

def return_book(request: HttpRequest, id):
    book = Book.objects.get(id=id)
    book.checked_out = False
    book.save()
    checkin = CheckOut.objects.filter(book=book).last()
    print(f'MOST RECENT CHECKOUT: {checkin}')
    checkin.date_returned = datetime.now()
    checkin.save()
    print(checkin)
    return redirect('/library/')

