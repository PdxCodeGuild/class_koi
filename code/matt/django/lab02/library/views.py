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

def author_detail(request, slug):
    author = Author.objects.get(slug=slug)
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

def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    author = book.author
    check_history = Checkout.objects.filter(book=book)
    status = check_history.last()
    if str(status.user) == str(request.user):
        same_user = True
    else:
        same_user = False
    genres = Genre.objects.filter(books=book)
    if request.method == 'POST':
        status_update = request.POST.get('status_update')
        user_name = request.user
        Checkout.objects.create(
            book=book,
            user=user_name,
            checkout=status_update,
        )
        return redirect('library:book_detail', slug=slug)
    context = {
        'book': book,
        'author': author,
        'check_history': check_history,
        'genres': genres,
        'status': status,
        'same_user': same_user,
    }
    return render(request, 'library/book_detail.html', context)

def history(request):
    check_history = Checkout.objects.all
    context = {
        'history': check_history,
    }
    return render(request, 'library/history.html', context)

def genre(request, slug):
    genre = Genre.objects.get(slug=slug)
    books = Book.objects.filter(genre=genre)
    context = {
        'genre': genre,
        'books': books,
    }
    return render(request, 'library/genre.html', context)

