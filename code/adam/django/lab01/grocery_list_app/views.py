from asyncio.windows_events import NULL
from datetime import date
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import GroceryItem
# Create your views here.

def index(request):
    if request.method == 'POST':
        print(request.POST)
        data = dict(request.POST)
        print(data)
        description = request.POST.get('description')

        item = GroceryItem.objects.create(
            description=description
        )

    grocery_list = GroceryItem.objects.all()
    completed_list = GroceryItem.objects.filter(completed=True)
    incomplete_list = GroceryItem.objects.filter(completed=False)

    context = {
        'grocery_list': grocery_list,
        'message': 'Grocery List',
        'completed_list': completed_list,
        'incomplete_list': incomplete_list,
    }

    return render(request, 'grocery_list_app/index.html', context)

def complete(request, id):
    grocery_item = GroceryItem.objects.get(id=id)
    print(grocery_item)
    # the following query would get you the first GroceryItem instance
    # with description='apples' and completed=True, or an error
    # item = GroceryItem.objects.get(description='apples', completed=True)
    grocery_item.completed = True
    grocery_item.completed_date = timezone.now()
    grocery_item.save()
    return redirect('/grocery_list_app')

def incomplete(request, id):
    grocery_item = GroceryItem.objects.get(id=id)
    print(grocery_item)
    # the following query would get you the first GroceryItem instance
    # with description='apples' and completed=True, or an error
    # item = GroceryItem.objects.get(description='apples', completed=True)
    grocery_item.completed = False
    grocery_item.completed_date = None
    grocery_item.save()
    return redirect('/grocery_list_app')

def delete(request, id):
    grocery_item = GroceryItem.objects.get(id=id)
    grocery_item.delete()
    return redirect('/grocery_list_app')



