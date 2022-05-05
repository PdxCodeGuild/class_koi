from django.shortcuts import render
from .models import Author, Book


def index(request):
    inventory = Book.objects.all()
    author = Author.objects.all()
    return render(request,'library/index.html',{'inventory':inventory, 'author':author})


    
