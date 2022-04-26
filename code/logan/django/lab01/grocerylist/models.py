from django.db import models

# Create your models here.
class Grocery(models.Model):
    description = models.CharField(max_length=200)
    created_date = models.DateField()
    last_name = models.CharField(max_length=200)