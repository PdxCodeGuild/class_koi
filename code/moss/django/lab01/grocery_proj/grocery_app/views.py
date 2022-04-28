from django.shortcuts import render
from .models import GroceryItem

def index (request):
    stuff = GroceryItem.objects.all()
    return render(request,'grocery_app/index.html',{'stuff':stuff})

