from asyncio.proactor_events import _ProactorSocketTransport
from tabnanny import verbose
from django.db import models

from django.utils import timezone
# Create your models here.


class Users(models.Model):
    user_name = models.CharField(max_length=40)

    def __str__(self):
        return self.user_name


class Posts(models.Model):
    posted_message = models.CharField(max_length=128, null=True, blank=True)
    posted_time = models.CharField(max_length=40, blank=True)
    author = models.ForeignKey(
        Users, on_delete=models.PROTECT, related_name='auth', blank=True, null=True)

    def __str__(self):
        return self.posted_message

    class Meta:
        verbose_name_plural = 'Posts'
