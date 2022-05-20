from django.db import models
from django.urls import reverse
from django.utils import timezone


class Authors(models.Model):
    author_name = models.CharField(max_length=40)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name_plural = 'Authors'


class Books(models.Model):

    name = models.CharField(max_length=60)
    publish_date = models.CharField(max_length=4)
    author = models.ForeignKey(
        Authors, on_delete=models.PROTECT, related_name='auth', blank=True, null=True)
<<<<<<< Updated upstream
    checked_out = models.BooleanField('available', default=False)
    who_checked_out = models.CharField(max_length=60, null=True)
    who_checked_out_time = models.CharField(max_length=60, null=True)
=======
    checked_out = models.BooleanField('available', default=False, blank=True)
>>>>>>> Stashed changes

    def __str__(self):

        return self.name

    class Meta:
        verbose_name_plural = 'Books'


class Checked_Book(models.Model):
    name = models.ForeignKey(
        Books, on_delete=models.PROTECT, related_name='title', blank=True, null=True)
    checked_out = models.BooleanField('available', default=False, blank=True)
    who_checked_out = models.CharField(max_length=60, null=True, blank=True)
    who_checked_out_time = models.DateTimeField(blank=True, null=True)
    who_checked_in_time = models.DateTimeField(blank=True, null=True)
    who_checked_in = models.CharField(max_length=60, null=True, blank=True)
