from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    publish_date = models.DateField('date published', null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    checked_out = models.BooleanField('checked-out', default=False)
    checked_out_date = models.DateField('date checked-out', null=True, blank=True)
    checked_in_date = models.DateField('date checked in', null=True, blank=True)

    def __str__(self):
        return f'{self.title} by {self.author}'

class Checkout(models.Model):
    checked_out_by = models.CharField(max_length=50)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)    
    


