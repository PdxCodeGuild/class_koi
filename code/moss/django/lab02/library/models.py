
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    pub_date = models.DateField()

    def __str__(self):
        return self.title

    

# class Member(models.Model):
#     book =
#     user =
#     checkout =
#     timestamp = 
