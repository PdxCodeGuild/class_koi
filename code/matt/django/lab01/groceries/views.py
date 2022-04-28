from django.shortcuts import render, redirect
from django.http import HttpResponse

from datetime import datetime

from .models import Grocery

def index(request):
    if request.method == 'POST':
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        note = request.POST.get('note')
        grocery = Grocery.objects.create(
            item=item,
            quantity=quantity,
            note=note,
        )
        return redirect('/groceries')

    groceries = Grocery.objects.all()
    groceries_complete = Grocery.objects.filter(completed=True)
    groceries_incomplete = Grocery.objects.filter(completed=False)
    context = {
        'groceries': groceries,
        'groceries_complete': groceries_complete,
        'groceries_incomplete': groceries_incomplete,
    }
    return render(request, 'groceries/index.html', context)

def detail(request, id):
    item = Grocery.objects.get(id=id)
    context = {
        'item': item,
    }
    return render(request, 'groceries/detail.html', context)

def complete(request, id):
    item = Grocery.objects.get(id=id)
    item.completed = True
    item.completed_date = datetime.now()
    item.save()
    return redirect(f'/groceries/{id}')

def delete(request, id):
    item = Grocery.objects.get(id=id)
    item.delete()
    return redirect(f'/groceries')

def uncomplete(request, id):
    item = Grocery.objects.get(id=id)
    item.completed = False
    item.completed_date = None
    item.save()
    return redirect(f'/groceries/{id}')
