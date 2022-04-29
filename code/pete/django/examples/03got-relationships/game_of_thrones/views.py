from django.shortcuts import render, redirect, get_object_or_404

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
    if request.method == 'POST':
        print(request.POST)
        character_name = request.POST.get('character_name')
        print('the name is ', character_name)
        Character.objects.create(
            name=character_name,
            house=house
        )
        return redirect('thrones:house', name=house.name.lower())
        # the following line would have the same effect
        return redirect(f'/{house.name}/')
    # house = House.objects.get(name=name.capitalize())
    context = {'house': house}
    return render(request, 'game_of_thrones/house.html', context)