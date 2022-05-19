from datetime import date, datetime

from django.views import generic
from django.db import models
from django.http import HttpResponse
from django.utils import timezone


class GroceryItem(models.Model):
    item = models.CharField(max_length=50, null=True)

    created_date = models.DateField(
        null=True, blank=True, default=timezone.now())

    quantity = models.IntegerField(null=True, default=0)

    completed_date = models.DateField(null=True, blank=True)

    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item
