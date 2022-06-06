from django.shortcuts import render, redirect
# you can use variables declared in your project settings.py by importing this settings object
from django.conf import settings

from .models import NutritionFacts
from .forms import NutritionFactsForm

def index(request):
    print(settings.API_KEY)
    print(settings.SECRET_MESSAGE)
    if request.method == 'POST':
        form = NutritionFactsForm(request.POST, request.FILES)
        if form.is_valid(): # returns true if the form has all required fields, etc.
            form.save()
            return redirect('nutrition:index')
        else:
            # form.errors is a dictionary of the errors
            message = 'Invalid Fields Provided'
            # you could put this message in a context dictionary
            # or something to give feedback to the user
        # # request.POST has the simple form inputs (text, numbers, etc.)
        # print(request.POST)
        # # request.FILES has more complex objects (like files)
        # print(request.FILES)

        # name = request.POST.get('name')
        # calories = request.POST.get('calories')
        # fat = request.POST.get('fat')
        # carbs = request.POST.get('carbs')
        # protein = request.POST.get('protein')
        # serving_size = request.POST.get('serving_size')

        # image = request.FILES.get('image')

        # NutritionFacts.objects.create(
        #     name=name,
        #     calories=calories,
        #     fat=fat,
        #     carbs=carbs,
        #     protein=protein,
        #     serving_size=serving_size,
        #     image=image,
        # )

        # return redirect('nutrition:index')
    form = NutritionFactsForm()
    context = {
        'nutrition_facts': NutritionFacts.objects.all(),
        'form': form,
        'secret_message': settings.SECRET_MESSAGE
    }
    return render(request, 'nutrition_database/index.html', context)