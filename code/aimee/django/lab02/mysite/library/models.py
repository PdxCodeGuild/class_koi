from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date created', auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, default=False)
    def __str__(self):
        return self.title

class CheckOut(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    checkout = models.BooleanField(default=False, blank=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    user = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.book}_{self.checkout}_{self.timestamp}'


