from xml.dom.pulldom import CHARACTERS
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from .models import Author, Book

def index(request: HttpRequest):
    authors = Author.objects.all()
    books = Book.objects.all()
    context = {
        'authors': authors,
        'characters': books,
    }
    return HttpResponse("hell, world, you are at the library") #request, '/library')


