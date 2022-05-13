from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from django.utils import timezone

from .models import Book, Author, User
# Create your views here.
def index(request):
    books = Book.objects.all()
    available_books = Book.objects.filter(checked_out = False)
    # show all users with the checkout bool as true and 
        # show only the first of those users
    check_in_books = User.objects.filter(checkout = True)
    hide_list = []
    show_list = []
    for index, i in enumerate(check_in_books):
        if(i in hide_list or i in show_list):
            continue
        elif(i.checkout == False and i in show_list):
            show_list.pop(i.name)
        elif(i.checkout == False and i not in hide_list):
            hide_list.append(i)
        elif(i.checkout == True and i not in hide_list and i not in show_list):
            show_list.append(i)
        # if(index == len(check_in_books)):
        #     hide_list = hide_list.clear()
    
    print(f'show list {show_list}')
    print(f'hide list {hide_list}')
    # hide_list = []
    # show_list = []

    library_history = User.objects.all()
    print(type(library_history))
    context = {
        'books': books,
        'available_books': available_books,
        # 'check_in_books': check_in_books,
        'check_in_books': show_list,
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

def user_checkin(request, show_list):
    if(request.method == 'POST'):
        name = request.POST.get('check_in_book')
        target_user:User = User.objects.filter(name = name).first()
        
        target_book:Book = Book.objects.filter(title = target_user.book).first()

        User.objects.create(name = target_user.name, book = target_user.book, checkout = False, timestamp = timezone.now())
        target_book.checked_out = False
        target_book.save()

        show_list = []
        return redirect('/')