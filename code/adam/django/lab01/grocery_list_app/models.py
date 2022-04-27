from django.db import models

# Create your models here.

class GroceryItem(models.Model):
    description = models.CharField(max_length=100)
    created_date = models.DateTimeField('date created')
    completed_date = models.DateTimeField('date completed')
    completed = models.BooleanField('completed')