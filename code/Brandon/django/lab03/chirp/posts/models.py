from tabnanny import verbose
from django.db import models

# Create your models here.


class Posts(models.Model):
    post = models.CharField(max_length=128)
    posted_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.post

    class Meta:
        verbose_name_plural = 'Posts'
