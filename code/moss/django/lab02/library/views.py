from django.shortcuts import render
from .models import Author, Book


def index(request):
    inventory = Book.objects.all()
    return render(request,'library/index.html',{inventory:inventory})


    
