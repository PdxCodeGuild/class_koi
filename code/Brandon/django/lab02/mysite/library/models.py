from django.db import models
from django.urls import reverse


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
    checked_out = models.BooleanField('available', default=True)
    who_checked_out = models.CharField(max_length=60, null=True)
    who_checked_out_time = models.CharField(max_length=60, null=True)

    def __str__(self):

        return self.name

    class Meta:
        verbose_name_plural = 'Books'
