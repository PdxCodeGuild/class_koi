import imp
from django.db import models
from django.contrib.auth.models import User

class ChirpPost(models.Model):
    #details of the post
    post_text = models.CharField(max_length=128)
    date_posted = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # date_edited = models.DateField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='chirps')

    def __str__(self):
        return f'{self.author}: {self.post_text}'




