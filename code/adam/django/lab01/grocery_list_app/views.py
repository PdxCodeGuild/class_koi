from audioop import reverse
from tkinter.tix import Tree
from django.shortcuts import render
from django.http import HttpResponseRedirect

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
        'message': 'Grocery List'
    }

    return render(request, 'grocery_list_app/index.html', context)

def complete(request, id):
    grocery_item = GroceryItem.objects.get(id=id)
    # the following query would get you the first GroceryItem instance
    # with description='apples' and completed=True, or an error
    # item = GroceryItem.objects.get(description='apples', completed=True)
    grocery_item.completed = True
    grocery_item.save()
    return render(request, 'grocery_list_app/index.html')



