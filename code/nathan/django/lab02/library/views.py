from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from django.utils import timezone

from .models import Book, Author, User
# Create your views here.
def index(request):
    books = Book.objects.all()
    available_books = Book.objects.filter(checked_out = False)
    check_in_books = Book.objects.filter(checked_out = True)

    library_history = User.objects.all()
    print(type(library_history))
    context = {
        'books': books,
        'available_books': available_books,
        'check_in_books': check_in_books,
        'library_history': library_history,
    }

    return render(request, 'index.html', context)

def user_checkout(request):
    if(request.method == 'POST'):
        # choose a book a user wants to check out
        book = request.POST.get('available_book')
        username = request.POST.get('user')

        target_book:Book = Book.objects.filter(title = book).first()

        User.objects.create(name = username, book = target_book, checkout = True, timestamp = timezone.now())
        target_book.checked_out = True
        target_book.save()

        return redirect('/')

def user_checkin(request):
    if(request.method == 'POST'):
        book = request.POST.get('check_in_book')
        name = request.POST.get('user')
        target_user:User = User.objects.filter(name = name).first()
        
        target_book:Book = Book.objects.filter(title = book).first()

        User.objects.create(name = target_user.name, book = target_user.book, checkout = False, timestamp = timezone.now())
        target_book.checked_out = False
        target_book.save()

        return redirect('/')