from django.shortcuts import render
from django.http import HttpResponse
from .models import Grocery

# Create views below
def index(request):
    latest_groceries = Grocery.objects.all()
    context = {'latest_groceries': latest_groceries}
    return render(request, "grocerylist/index.html", context)

def complete(request):
    return HttpResponse("you're completing, baby")

def delete(request):
    return HttpResponse("you're deleting, baby")