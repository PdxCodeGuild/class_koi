from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import GroceryItem

def index(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('users:login')
        description = request.POST.get('description')
        GroceryItem.objects.create(
            description=description,
            user=request.user
            # created_date=timezone.now(), # not needed due to change in models
        )
        return redirect('groceries:home')
    context = {}
    if request.user.is_authenticated:
        groceries = request.user.grocery_items.all()
        context = {
            'groceries_complete': groceries.filter(completed=True),
            'groceries_incomplete': groceries.filter(completed=False),
        }
    return render(request, 'grocery_list/index.html', context)

@login_required
def toggle_complete(request, id):
    # item = GroceryItem.objects.get(id=id)
    item = get_object_or_404(GroceryItem, id=id) # raises a 404 instead of a 500 if the object doesn't exist
    # this is a little shortcut that will flip the boolean (True or False) to the other possible value
    if item.user != request.user:
        return redirect('groceries:home')
    item.completed = not item.completed
    # if item.completed == False:
    #     item.completed = True
    # elif item.completed == True:
    #     item.completed = False
    item.save()
    return redirect('groceries:home')

@login_required
def delete(request, id):
    item = get_object_or_404(GroceryItem, id=id) # raises a 404 instead of a 500 if the object doesn't exist
    if item.user != request.user:
        return redirect('groceries:home')
    item.delete()
    return redirect('groceries:home')
