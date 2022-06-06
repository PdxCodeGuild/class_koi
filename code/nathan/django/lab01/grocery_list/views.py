from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.utils import timezone

from .models import GroceryItem
# Create your views here.
def index(request):

    grocery_list = GroceryItem.objects.all()
    completed_list = GroceryItem.objects.filter(completed=True)
    incompleted_list = GroceryItem.objects.filter(completed=False)

    context = {
        'grocery_list' : grocery_list,
        'completed_list' : completed_list,
        'incompleted_list' : incompleted_list,
    }

    return render(request, 'index.html', context)

def add_grocery(request):
    if(request.method == 'POST'):
        description = request.POST.get('description')
        grocery = GroceryItem.objects.create(description = description)
    return redirect('/')


def mark_complete(request):
    if(request.method == 'POST'):
        grocery = request.POST.get('grocery')
        current_grocery:GroceryItem = GroceryItem.objects.filter(description = grocery).first()
        print(current_grocery)
        current_grocery.completed_date = timezone.now()
        current_grocery.completed = True
        current_grocery.save()
    return redirect('/')

def delete_grocery(request):
    if(request.method == 'POST'):
        grocery = request.POST.get('grocery')
        current_grocery:GroceryItem = GroceryItem.objects.filter(description = grocery).first()
        current_grocery.delete()
        return redirect('/')