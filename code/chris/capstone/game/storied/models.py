from django.db import models

class Story(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Stories'

class StoryPrompt(models.Model):
    prompt = models.TextField()
    # user_options = models.CharField(max_length=200)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='Prompts')

    def __str__(self):
        return f'{self.story} prompt {self.id}'

