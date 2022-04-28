from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date created', auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

class CheckedOut(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    checkout = models.BooleanField(default=False)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    user = models.CharField(max_length=50)