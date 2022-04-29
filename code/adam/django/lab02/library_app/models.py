from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=50)
    publish_date = models.DateField('date published', default=)

    def __str__(self):
        return self.name

class Author(models.Model):


