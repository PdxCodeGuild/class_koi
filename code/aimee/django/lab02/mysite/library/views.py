from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Author, Book, CheckOut
from .forms import CheckOutForm

def index(request):
    """main page"""
    if request.method == 'POST':
        form = CheckOutForm(request.POST)
        if form.is_valid():
            form.save()
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'books':books,
    }
    return render(request, 'library/index.html', context)

def details(request, id):
    """book details, if available/not"""
    book = Book.objects.get(id=id)
    author = book.author
    history = CheckOut.objects.filter(book=book)
    status = history.last()
    if request.method == 'POST':
        status_update = request.POST.get('status_update')
        username = request.POST.get('username')
        CheckOut.objects.create(
            book=book, user=username, checkout=status_update,
        )
        return redirect('library/details/', id=id)
    context = {
        'book':book,
        'author':author,
        'history':history,
        'status':status,
        }
    return render(request, 'library/details.html', context)

# not finished
def checkouts(request, id):
    checked_out = CheckOut.objects.get(id=id)
    # if ID is 1, book is checked out
    checked_out.checkout = True
    checked_out.save()
    context = {'checked_out':checked_out,}
    return redirect('/library/')

