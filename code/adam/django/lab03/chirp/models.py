import imp
from django.db import models
from django.contrib.auth.models import User

class ChirpPost(models.Model):
    #details of the post
    author = models.CharField(max_length=50)
    post_text = models.CharField(max_length=128)
    date_posted = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # date_edited = models.DateField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.author}: {self.date_posted}'




