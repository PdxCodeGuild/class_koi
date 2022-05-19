from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.utils.timezone import make_aware

from datetime import datetime, timezone

from .models import GroceryItem

def index(request: HttpRequest):
    if request.method == 'POST': # completes an item
        grocery_item = request.POST.get('name')
        complete_date = make_aware(datetime.now())
        item = GroceryItem.objects.filter(item_text=grocery_item).update(completed=True, completed_date=complete_date)
        
        return redirect('/grocery_list_app')
    
    groceries = GroceryItem.objects.all()
    context = {
        'groceries': groceries,
        'message': 'Welcome to the Grocery List'
    }
    return render(request, 'grocery_list_app/index.html', context)

def detail(request:HttpRequest, id: int):
    if request.method == 'POST': # deletes a record
        grocery_item = request.POST.get('name')
        GroceryItem.objects.filter(item_text=grocery_item).delete()
        return redirect('/grocery_list_app')
    
    grocery = GroceryItem.objects.get(id=id)
    context = {
        'grocery': grocery,
    }
    return render(request, 'grocery_list_app/detail.html', context)

def add(request: HttpRequest):
    if request.method == 'POST': # adds an item
        name = request.POST.get('item')
        created_date = make_aware(datetime.now())
        item = GroceryItem.objects.create(
            item_text=name,
            created_date=created_date,
            completed=False,
        )
        return redirect('/grocery_list_app')

    return render(request, 'grocery_list_app/add.html')

