from .forms import Addbookform, Checkinoutform
from turtle import title
from django.shortcuts import render, redirect
from.models import Book, Checkinout


def index(request):
    if request.method == 'POST':
        print(request.POST)
        form = Checkinoutform(request.POST)
        checkoutlist = Checkinout.objects.all()
        if form.is_valid():
            
            
            title = form.cleaned_data['title']
            name = form.cleaned_data['name']
            lengthofcheckout = form.cleaned_data['lengthofcheckout']
            checkouttime = form.cleaned_data['checkouttime']
            in_out = form.cleaned_data['in_out']
            
            listitem = Checkinout(title=title, name=name,in_out=in_out)
            listitem.save()
            
            form.save()
            checkoutdict = {
                'checkoutlist':checkoutlist
            }
            return render (request,'library/checkout.html', checkoutdict)
        else:
            message = 'Invalid Fields Provided'
    form = Checkinoutform()
    booklist = Book.objects.all()
    thisform = Addbookform(request.POST)
    context = {
        'booklist': booklist,
        'message': 'Welcome to the Library',
        'form': form,
        'thisform':thisform,
        

    }
    return render(request, 'library/index.html', context)


def addbook(request):
    if request.method == 'POST':
        thisform = Addbookform(request.POST)
        if thisform.is_valid():
            title = thisform.cleaned_data['title']
            pub_date = thisform.cleaned_data['pub_date']
            author = thisform.cleaned_data['author']

            book = Book(title=title, pub_date=pub_date, author=author)
            book.save()
        return render(request, 'library/index.html', {'thisform': thisform})
