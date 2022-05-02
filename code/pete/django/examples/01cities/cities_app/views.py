from django.shortcuts import render, redirect

from .models import City

# from django.http import HttpResponse

# Flask version:
# @app.route('/')
# def index():
#     return 'hello world' # in flask you can just return a string

# Django Version
# def index(request):
#     return HttpResponse('<h1>hello world</h1>')

def index(request):
    # declaring a variable
    message = 'Django is a Python web framework!'
    # creating a context dictionary, when the app sees
    # {{ message }} in the template, it wil fill that in
    # with the message value from this dictionary
    context = {
        'message': message
    }
    return render(request, 'cities_app/index.html', context)

def cities(request):
    # City.object is a manager.  You can use it as an interface to the database
    # City.objects.all is just one method that it has
    cities = City.objects.all() # returns a list-like object of all the cities in the database
    print(cities) # <QuerySet [<City: Fargo>, <City: Portland>]>
    # for city in cities:
    #     print(city.climate) 

    context = {
        'cities': cities
    }
    return render(request, 'cities_app/cities.html', context)

def add_city(request):
    if request.method == 'POST':
        # request.POST is a QueryDict, a dictionary-like object, of the information submitted to a form on a post request
        print(request.POST) # <QueryDict: {'csrfmiddlewaretoken': ['qENG5Altj9nMUw3MgvN0OYKbTSCfQyHH6t3cviXnL1K5WzRuh5vcPgrko9TZea6b'], 'name': ['Kansas City'], 'country': ['USA'], 'population': ['508090'], 'food': ['Barbecue'], 'mayor': ['Quinton Lucas'], 'climate': ['temperate']}>
        # you can use request.POST['key'] or request.POST.get('key')
        name = request.POST.get('name')
        country = request.POST.get('country')
        population = request.POST.get('population')
        food = request.POST.get('food')
        mayor = request.POST.get('mayor')
        climate = request.POST.get('climate')
        print(name, country, population, food, mayor, climate)

        new_city = City.objects.create(
            name=name,
            country=country,
            population=population,
            food=food,
            mayor=mayor,
            climate=climate
        )
    # redirect can take in multiple object types
    # given a string, it will try and match that url
    # and act as though sent to 127.0.0.1:8000/cities
    return redirect('/cities')