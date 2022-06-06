from sqlite3 import Timestamp
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books')
    checked_out = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=200)
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='books', null = True)
    checkout = models.BooleanField(default=False)
    timestamp = models.DateTimeField(null = True)

    def __str__(self):
        return self.name
    
    @property
    def get_book_title(self):
        return self.book.title