from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Author, Book, Checkout


def index(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    context = {
        'authors': authors,
        'books': books,
    }
    return render(request,'library/index.html', context)

def author(request, id:int):
    author = get_object_or_404(Author, id=id)
    context = {'author': author}
    return render(request, 'library/author.html', context)

def book(request, id:int):
    book = get_object_or_404(Book, id=id)
    checkout_ledger = Checkout.objects.filter(book=book)
    current_checkout = checkout_ledger.last()
    if request.method =='POST':
        lend_book = request.POST.get('lend_book')
        user = request.POST.get('user')

        Checkout.objects.create(
            book = book,
            user = user,
            checkout = lend_book
        )
        return redirect('library:book', id=id)

    context = {
        'book': book,
        'checkout_ledger': checkout_ledger,
        'current_checkout': current_checkout,
    }
    return render(request,'library/book.html', context)

    
