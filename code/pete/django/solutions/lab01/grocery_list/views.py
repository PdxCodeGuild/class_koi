from django.shortcuts import render, redirect, get_object_or_404

from .models import GroceryItem

def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        GroceryItem.objects.create(
            description=description,
            # created_date=timezone.now(), # not needed due to change in models
        )
        return redirect('groceries:home')
    context = {
        'groceries_complete': GroceryItem.objects.filter(completed=True),
        'groceries_incomplete': GroceryItem.objects.filter(completed=False),
    }
    return render(request, 'grocery_list/index.html', context)

def toggle_complete(request, id):
    # item = GroceryItem.objects.get(id=id)
    item = get_object_or_404(GroceryItem, id=id) # raises a 404 instead of a 500 if the object doesn't exist
    # this is a little shortcut that will flip the boolean (True or False) to the other possible value
    item.completed = not item.completed
    # if item.completed == False:
    #     item.completed = True
    # elif item.completed == True:
    #     item.completed = False
    item.save()
    return redirect('groceries:home')

def delete(request, id):
    item = get_object_or_404(GroceryItem, id=id) # raises a 404 instead of a 500 if the object doesn't exist
    item.delete()
    return redirect('groceries:home')
