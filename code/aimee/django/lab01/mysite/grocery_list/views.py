from ast import Add
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import GroceryItem
from .forms import AddItem, GroceryItemForm

def index(request):
	if request.method == 'POST':
		form = GroceryItemForm(request.POST)
		print(form)
		if form.is_valid():
			form.save()

	grocery_list = GroceryItem.objects.order_by('pub_date')[:20]
	completed_list = GroceryItem.objects.filter(check_completed=True)
	incomplete_list = GroceryItem.objects.filter(check_completed=False)
	template = loader.get_template('grocery_list/index.html')
	form = GroceryItemForm()
	context = {
		'grocery_list':grocery_list,
		'form':form,
		'completed_list':completed_list,
		'incomplete_list':incomplete_list,
	}
	return render(request, 'grocery_list/index.html', context)

def detail(request, id):
	grocery_item = GroceryItem.objects.get(id=id)
	context = {
		'grocery_item':grocery_item,
	}
	return render(request, 'grocery_list/detail.html', context)

def complete(request, id):
	item = GroceryItem.objects.get(id=id)
	item.check_completed = True
	item.done_date
	item.save()
	# return render(request, 'grocery_list/complete.html')
	return redirect(f'/detail/{id}')

def delete(request, id):
	item = GroceryItem.objects.get(id=id)
	item.delete()
	return redirect(f'grocery_list/')
