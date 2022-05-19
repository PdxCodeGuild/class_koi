from datetime import date
from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest

from .models import GroceryItem


def index (request):
	grocery_list = GroceryItem.objects.all() 
	completed_list = GroceryItem.objects.filter(completed=True)
	
	context = {
    'grocery_list': grocery_list,
    'groceries_complete': completed_list,
    'message': 'Welcome to Dans Grocery'
	}
	return render(request, 'myapp/index.html', context)

def add_item(request):
	if request.method == 'POST':
     
		print(request.POST) 
		name = request.POST.get('name')
		description = request.POST.get('description')
		create = request.POST.get('created_date')
		item_bool = request.POST.get('item_boolean')
		print (name, description, create, item_bool)
    
	new_item = GroceryItem.objects.create(
		item_name = name,
		item_description = description,
		created_date = create,
		
			
    )
    
	return redirect('/')


def complete(request):
    print (request.POST)
    id = request.POST.get('id')
    item = GroceryItem.objects.get(id = int(id))
    item.completed = True
    item.save()
    return redirect('/')
    
    
def delete(request):
    name = request.POST.get('name')
    item = GroceryItem.objects.get(item_name = name)
    item.delete()
    return redirect('/')