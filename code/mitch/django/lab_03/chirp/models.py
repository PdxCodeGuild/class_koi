from django.db import models
from django.contrib.auth.models import User

class ChirpPost(models.Model):
    text = models.CharField(max_length=128)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='grocery_items')
    
    def __str__(self):
        return f'{self.user}@ {self.date}: {self.text}'
