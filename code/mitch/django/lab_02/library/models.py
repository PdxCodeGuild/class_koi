from django.db import models
from django.forms import DateField, DateTimeField

# Create your models here.
    
class Author(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=60)
    publish_date = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books')
    

    def __str__(self):
        return self.title

