from datetime import datetime
from sqlite3 import Timestamp
from django.db import models
from django.forms import DateField, DateTimeField

# Create your models here.
    
class Author(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=80)
    publish_date = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books')
    

    def __str__(self):
        return self.title

class Checkout(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    username = models.CharField(max_length=60)
    checkout = models.BooleanField(default=False, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return f'{self.checkout}_{self.timestamp}'
