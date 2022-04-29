from datetime import date
from django.shortcuts import get_object_or_404, redirect, render

from django.views import generic
from .models import GroceryItem
from django.utils import timezone

from django.http import HttpRequest, HttpResponse
from django.urls import reverse


# class IndexView(generic.ListView):
#     model = GroceryItem
#     template_name = 'grocerylist/index.html'
#     context_object_name = 'latest_grocery_list'

def index(request):

    if request.method == 'POST':  # this code will only run if it gets a post request
        print(request.POST)
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        created_date = request.POST.get('created_date')
        completed_date = request.POST.get('completed_date')
        gitem = GroceryItem.objects.create(
            item=item,
            quantity=quantity,
            created_date=created_date,
            completed_date=completed_date,
        )
        GroceryItem.completed_date = timezone.now()
    groceries = GroceryItem.objects.all()
    context = {
        'groceries': groceries
    }
    return render(request, 'grocerylist/index.html', context)

# def get_queryset(self):
#     # """
#     # return the last five published questions (not including those set to be published in the future).
#     # """
#     return GroceryItem.objects.filter(
#         created_date__lte=timezone.now()
#     ).order_by('-created_date')[:10]


# class CreateView(generic.CreateView):
#     model = GroceryItem
#     template_name = 'grocerylist/index.html'
#     context_object_name = 'latest_grocery_list'

    # Save the new GroceryItem to the databse!

    # What else?  Return, redirect?  It's up to you!

    # Here you'll put the code that you want to run for a GET request
    # How do you want to get the necessary items from the database?
    # Here are 3 different queries that return different QuerySets
    # You can use one of these or a combination to put into your context
    # dictionary and render the template

    #     # the context dictionary will have all the objects
    #     # you want to render in your template
    #     # the return line will render the template
    # return render(request, 'grocerylist/index.html', context)


"""
Note: there are multiple ways to complete/delete GroceryItems
The following is just a suggestion
"""


def glist(request, id: int):
    print(id)
    groceries = GroceryItem.objects.get(id=id)
    context = {
        'groceries': groceries,
        'message': 'Welcome to Grocery Planner',
    }

    # if request.method == 'POST':  # this code will only run if it gets a post request
    #     print(request.POST)
    #     # item = request.POST.get('item')
    #     # quantity = request.POST.get('quantity')
    #     # created_date = request.POST.get('created_date')
    #     # completed_date = request.POST.get('completed_date')
    #     # gitem = GroceryItem.objects.create(
    #     #     completed_date=completed_date,
    #     # )
    #     GroceryItem.completed = True
    return render(request, 'grocerylist/glist.html', context)


def complete(request, id):
    # use the id to get the object from the database
    groceries = GroceryItem.objects.get(id=id)
    # context = {
    #     'groceries': groceries,
    # }
    # change it's completed attribute to True
    item = GroceryItem.objects.get(id=id)
    # save it
    item.completed = True
    item.save()
    # redirect back to the home page
    # return redirect('')
    return render(request, 'grocerylist/glist.html')


def delete(request, id):
    # groceries = GroceryItem.objects.get(id=id)
    # context = {
    #     'groceries': groceries,
    # }
    item = GroceryItem.objects.get(id=id)
    item.delete()
    # use the id to get the object from the database
    # delete it
    # redirect back to the home page
    return render(request, 'grocerylist/glist.html')
