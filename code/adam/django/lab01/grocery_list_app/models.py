import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class GroceryItem(models.Model):
    description = models.CharField(max_length=100)
    created_date = models.DateTimeField('date created', default=timezone.now)
    completed_date = models.DateTimeField('date completed', null=True, blank=True)
    completed = models.BooleanField('completed', default=False)
    def __str__(self):
        return self.description
