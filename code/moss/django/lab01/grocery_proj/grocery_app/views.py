from django.shortcuts import render
from .models import GroceryItem

def index (request):
    completed_items = GroceryItem.objects.filter(completed=True).order_by('completed_date')
    incomplete_items = GroceryItem.objects.filter(completed=False).order_by('created_date')
    context = {
        'completed_items': completed_items,
        'incomplete_items': incomplete_items,
    }

    return render(request,'grocery_app/index.html', context)

