from django.conf import settings
from django.db import models
from django.utils import timezone

from datetime import datetime

class GroceryItem(models.Model):
    item_text = models.CharField(max_length=200)
    created_date = models.DateTimeField('date added', default=datetime.now)
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField('date completed', null=True, blank=True)

    def __str__(self): # this determines how the object will appear when turned into a string
        # the default is ModelName (id) (City(1), City(2), etc)
        # particularly helpful in the admin panel
        return self.item_text


# class ItemStatus(models.Model):
#     grocery_item = models.ForeignKey(GroceryItem, on_delete=models.CASCADE)
#     completed = models.BooleanField(default=False)

#     def __str__(self): # this determines how the object will appear when turned into a string
#         # the default is ModelName (id) (City(1), City(2), etc)
#         # particularly helpful in the admin panel
#         return self.name
