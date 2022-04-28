from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.utils import timezone
from .models import Grocery

# Create views below
def index(request: HttpRequest):
    if request.method == 'POST': # this code will only run if it gets a post request
        print(request.POST)
        name = request.POST.get('name')
        # created_date = request.POST.get('created date')
        # completed_date = request.POST.get('completed date')
        # completed = request.POST.get('completed')
        # Model.object.create(**kwargs) will create a new instance
        # of that model and save it to the database

        groc = Grocery.objects.create(
            name=name,
            # created_date = created_date,
            # completed_date = completed_date,
            # completed = completed,
            )
        return redirect('/grocerylist')


    latest_groceries = Grocery.objects.all()
    completed_list = Grocery.objects.filter(completed=True)
    incompleted_list = Grocery.objects.filter(completed=False) 
    context = {
        'latest_groceries': latest_groceries,
        'completed_list' : completed_list,
        'incompleted_list' : incompleted_list,
    }
    
    return render(request, "grocerylist/index.html", context)

def complete(request, id: int):
    """
    Just imagine how cool a comment would be here...
    """
    grocery = Grocery.objects.get(id=id)
    if grocery.completed == False:
        grocery.completed = True
        grocery.completed_date = timezone.now()
    else:
        grocery.completed = False
        grocery.completed_date = None
    grocery.save()

    return redirect('/grocerylist/')


    # return HttpResponse("you're completing, baby")
    ...


def delete(request, id: int):
    grocery = Grocery.objects.get(id=id)
    grocery.delete()
    return redirect('/grocerylist/')
    ...