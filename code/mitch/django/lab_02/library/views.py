from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse

from .models import Author, Book, Checkout

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
    checkout_log = Checkout.objects.filter(book=book)
    current_checkout = checkout_log.last()
    if request.method == "POST":
        borrowed_bool = request.POST.get('borrowed_bool')
        username = request.POST.get('username')
        
        Checkout.objects.create(
            book = book,
            username = username,
            checkout = borrowed_bool
        )
        return redirect('library:book')
    
    context = {
        "book": book,
        "checkout_log": checkout_log,
        "current_checkout": current_checkout,
    }
    return render(request, 'library/book.html', context)
    