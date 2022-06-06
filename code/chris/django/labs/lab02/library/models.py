from django.db import models

class Author(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=100)

class Book(models.Model):
    def __str__(self):
        return self.title
    
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books')
    date_published = models.DateField('date published', null=True, blank=True)
    checked_out = models.BooleanField(default=False)

class CheckOut(models.Model):
    def __str__(self):
        return f'{self.book} {self.reader} {self.date_checked_out}'
    
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='checkouts')
    reader = models.CharField(max_length=100, null=True, blank=True)
    date_checked_out = models.DateField('date checked out')
    date_returned = models.DateField('date returned', null=True, blank=True)
