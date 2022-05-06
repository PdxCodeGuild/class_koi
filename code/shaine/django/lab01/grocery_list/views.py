from ast import Return
from itertools import count
from multiprocessing import context
from django.shortcuts import render,  redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm, UpdateForm




# Create your views here.

def index(request):
    items = Item.objects.all()
    count_items = items.count()
    

    completed_item = Item.objects.filter(complete=True)
    count_completed_item = completed_item.count()

    count_needed = count_items - count_completed_item


    if request.method=='POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ItemForm()

    context = {
        'items': items,
        'form': form,
        'count_items': count_items,
        'count_completed_item': count_completed_item,
        'count_needed': count_needed,  
    }
    return render(request, 'grocery/index.html', context)

def update(request, pk):
    entry = Item.objects.get(id=pk)

    if request.method=='POST':
        form = UpdateForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UpdateForm(instance=entry)
    context = {
        'form': form,
    }
    return render(request, 'grocery/update.html', context)

def delete(request, pk):
    entry = Item.objects.get(id=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('/')
    return render(request, 'grocery/delete.html')


# Item.set_complete()