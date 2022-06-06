from venv import create
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone

from .models import GroceryItem

def index(request: HttpRequest):
    if request.method == "POST":
        
        description = request.POST.get('description')


        GroceryItem.objects.create(
            description=description,
        )
        
        return redirect('/')

    grocery_list = GroceryItem.objects.all()
    completed_list = GroceryItem.objects.filter(completed=True)
    incomplete_list = GroceryItem.objects.filter(completed=False)
    
    context = {
        "grocery_list": grocery_list,
        "completed_list": completed_list,
        "incomplete_list": incomplete_list
        
    }
    return render(request, 'grocery_list_app/index.html', context)
    

def complete(request, id):
    item = GroceryItem.objects.get(id=id)
    item.completed_date = timezone.now()
    item.completed = True
    item.save()
    return redirect('/')


def delete(request, id):
    item = GroceryItem.objects.get(id=id)
    item.delete()
    return redirect('/')
    
    
def undo(request, id):
    item = GroceryItem.objects.get(id=id)
    item.completed = False
    item.completed_date = None
    item.save()
    return redirect('/')
    
    
    
    
    
    
    
    