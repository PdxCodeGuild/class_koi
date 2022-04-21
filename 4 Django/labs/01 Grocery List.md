# Lab 01: Grocery List

### Let's create a simple grocery list app. 

This can be done with a single app called `grocery_list` and model called `GroceryItem` which contains a text description, a created date, a completed date, and a boolean representing whether it was completed.

Your database would look something like this:
|id|description|created_date|completed_date|completed|
|--|-----------|------------|--------------|---------|
| 1|     apples|  2021-09-09|    2021-09-09|     True|
| 2|    bananas|  2021-09-09|          NULL|     False|

The user should be presented with an input field and a button (in a form). When the user clicks the button, it should save the data to the server and show the newly-added item in the list. The user should be presented with a list of incomplete items and a list of complete items. The user should be able to mark an item complete/incomplete and be able to delete an item.

Here is some optional* starter code for your app's `views.py`:

##### *This is not the only way to structure your views for this lab!  Just a suggestion if you don't know where to start.

```py
from django.shortcuts import render

from .models import GroceryItem

def index(request):
	if request.method == 'POST':
		# If there's a POST request, that means the user
		# has submitted a new GroceryItem for the database
		# How do you parse it?
		print(request.POST) # this will show the post request's
		# QueryDict, a dictionary-like object with the contents
		# of the form data
		data = dict(request.POST) # Optionally, turn the QueryDict
		print(data) # into a plain Python dictionary

		# Save the new GroceryItem to the databse!

		# What else?  Return, redirect?  It's up to you!

	# Here you'll put the code that you want to run for a GET request
	# How do you want to get the necessary items from the database?
	# Here are 3 different queries that return different QuerySets
	# You can use one of these or a combination to put into your context
	# dictionary and render the template

	grocery_list = GroceryItem.objects.all() # get all the GroceryItems
	completed_list = GroceryItem.objects.filter(completed=True) # get the completed GroceryItems
	incomplete_list = GroceryItem.objects.filter(completed=False) # get the completed GroceryItems

	context = {???} # the context dictionary will have all the objects
	# you want to render in your template
	# the return line will render the template
	return render(request, 'grocery_list/index.html', context)

"""
Note: there are multiple ways to complete/delete GroceryItems
The following is just a suggestion
"""

def complete(request, id):
	# use the id to get the object from the database
	# change it's completed attribute to True
	# save it
	# redirect back to the home page
	...

def delete(request, id):
	# use the id to get the object from the database
	# delete it
	# redirect back to the home page
	...

```

Here is a suggested series of steps to take to complete the lab

1. Get your urls and views to connected.  Render a simple template or return an `HttpResponse` so you know things are hooked up.
2. Make your `GroceryItem` model
3. Run `py manage.py createsuperuser` so you have an admin account.
4. In the admin panel, add some items to the database.
5. Create your home page.  It should show all of the grocery items.
6. Add a form so the user can submit new ones.
7. In the admin panel, mark some of the items as complete.
8. Either:
	1. Show 2 lists (incomplete and complete).
	2. Show 1 list with complete items marked (i.e.: crossed-out).
9. Add functionality for the user to complete/delete items.
