from django.db import models


class Author(models.Model):
    author = models.CharField(max_length=40)

    def __str__(self):
        return self.author


class Books(models.Model):
    name = models.CharField(max_length=60)
    publish_date = models.DateField(null=True)
    author = models.ForeignKey(Author,
                               on_delete=models.PROTECT, related_name='authors')
    checked_out = models.BooleanField('available', default=True)

    other_books = models.ManyToManyField(
        Author, related_name='other_books', blank=True)

    def __str__(self):
        checked_status = 'available' if self.checked_out else 'unavailable'
        return self.name
