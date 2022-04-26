from django.shortcuts import render
from django.http import HttpResponse

from .models import Author, Book

def index(request):
    authors = Author.objects.all
    books = Book.objects.all
    context = {
        'message': 'Hello world!',
        'authors': authors,
        'books': books,
    }
    return render(request, 'library/index.html', context)