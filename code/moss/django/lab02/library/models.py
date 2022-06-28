
from django.db import models
from django.utils import timezone
class Author(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author,on_delete=models.PROTECT, related_name ='books')
    pub_date = models.DateField()

    def __str__(self):
        return self.title

class Checkout(models.Model):
    book = models.ForeignKey(Book,on_delete=models.PROTECT,)
    user = models.CharField(max_length=50)
    checkout = models.BooleanField(null=False, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
