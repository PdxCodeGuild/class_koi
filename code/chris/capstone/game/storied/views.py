from django.shortcuts import render
from django.http import HttpResponse

from .models import StoryPrompt

def index(request):
    story_prompts = StoryPrompt.objects.all()
    
    context = {
        'story_prompts': story_prompts,
    }
    return render(request, 'storied/index.html', context)


