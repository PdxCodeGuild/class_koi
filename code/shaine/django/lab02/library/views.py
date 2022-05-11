from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import  CheckOutForm
# Create your views here.


def index(request):
    books = Book.objects.all()
    

    context = {
        'books': books,

    }
    return render(request, 'library/index.html', context)

def check_out(request, pk):
    entry = Book.objects.get(id=pk)
    title = entry.title
    user = entry.user

    if request.method=='POST':
        form = CheckOutForm(request.POST, instance=entry)
        if form.is_valid():
            entry.set_checkout()
            form.save()
            return redirect('/')
    else:
        form = CheckOutForm(instance=entry)
    context = {
        'form': form,
        'title': title,
        'user': user,
    }
    return render(request, 'library/check_out.html', context)

def check_in(request, pk):
    entry = Book.objects.get(id=pk)
    title = entry.title
    user = entry.user

    if request.method=='POST':
        form = CheckOutForm(request.POST, instance=entry)
        if form.is_valid():
            entry.set_checkin()
            form.save()
            return redirect('/')
    else:
        form = CheckOutForm(instance=entry)
    context = {
        'form': form,
        'title': title,
        'user': user,
    }
    return render(request, 'library/check_in.html', context)
