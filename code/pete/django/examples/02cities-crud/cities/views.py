from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from .models import City

# every django view takes in a request and returns a response

def index(request: HttpRequest): # : HttpRequest is NOT required, it just gives typing hints
    if request.method == 'POST': # this code will only run if it gets a post request
        print(request.POST)
        name = request.POST.get('name')
        population = request.POST.get('population')
        climate = request.POST.get('climate')
        # Model.object.create(**kwargs) will create a new instance
        # of that model and save it to the database
        city = City.objects.create(
            name=name,
            population=population,
            climate = climate
        )
        # print('*' * 40)
        # print(name)
        return redirect('/cities')

    # cities = ['Portland', 'KC', 'Fargo', 'Detroit', 'Seoul']
    cities = City.objects.all() # Model.objects.all() returns a QuerySet of all the models from that table

    # the context dictionary tells the template what to fill in
    # when it sees a {{ variable_name }}
    context = {
        'cities': cities,
        'message': 'Welcome to the Cities Database'
    }
    
    return render(request, 'cities/index.html', context)

# if you get a TemplateDoesNotExist error, make sure your app is registered
# in INSTALLED_APPS in the settings.py of the project folder