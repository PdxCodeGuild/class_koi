from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

class Checkout(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    checkout = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.book}_{self.checkout}_{self.timestamp}'

class Genre(models.Model):
    genre = models.CharField(max_length=50)
    books = models.ManyToManyField(Book, blank=True)
    
    def __str__(self):
        return self.genre