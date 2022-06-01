from django.contrib import admin

from .models import Story, StoryPrompt

admin.site.register(Story)
admin.site.register(StoryPrompt)
