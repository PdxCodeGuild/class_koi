from django.shortcuts import render, get_object_or_404

from .models import House, Character

def index(request):
    houses = House.objects.all()
    characters = Character.objects.all()
    context = {
        'houses': houses,
        'characters': characters,
    }
    return render(request, 'game_of_thrones/index.html', context)

def house(request, name:str):
    house = get_object_or_404(House, name=name.capitalize())
    # house = House.objects.get(name=name.capitalize())
    context = {'house': house}
    return render(request, 'game_of_thrones/house.html', context)