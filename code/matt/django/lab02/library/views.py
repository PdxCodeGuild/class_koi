from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Author, Book, Checkout, Genre

def index(request):
    authors = Author.objects.all
    books = Book.objects.all
    context = {
        'message': 'Welcome to the Library!',
        'authors': authors,
        'books': books,
    }
    return render(request, 'library/index.html', context)

def authors(request):
    authors = Author.objects.all
    context = {
        'authors': authors,
    }
    return render(request, 'library/authors.html', context)

def author_detail(request, id):
    author = Author.objects.get(id=id)
    books = Book.objects.filter(author=author)
    context = {
        'author': author,
        'books': books,
    }
    return render(request, 'library/author_detail.html', context)

def books(request):
    books = Book.objects.all
    context = {
        'books': books,
    }
    return render(request, 'library/books.html', context)

def book_detail(request, id):
    book = Book.objects.get(id=id)
    author = book.author
    check_history = Checkout.objects.filter(book=book)
    status = check_history.last()
    genres = Genre.objects.filter(books=book)
    if request.method == 'POST':
        status_update = request.POST.get('status_update')
        user_name = request.POST.get('user_name')
        Checkout.objects.create(
            book=book,
            user=user_name,
            checkout=status_update,
        )
        return redirect('library:book_detail', id=id)
    context = {
        'book': book,
        'author': author,
        'check_history': check_history,
        'genres': genres,
        'status': status,
    }
    return render(request, 'library/book_detail.html', context)

def history(request):
    check_history = Checkout.objects.all
    context = {
        'history': check_history,
    }
    return render(request, 'library/history.html', context)

