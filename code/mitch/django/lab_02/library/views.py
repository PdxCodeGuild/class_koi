from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Author, Book

def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'books' : books,
        'authors' : authors,
    }
    return render(request, 'library/index.html', context)

def author(request, id:int):
    author = get_object_or_404(Author, id=id)
    context = {"author": author}
    return render(request, 'library/author.html', context)

def book(request, id:int):
    book = get_object_or_404(Book, id=id)
    context = {"book": book}
    return render(request, 'library/book.html', context)
    