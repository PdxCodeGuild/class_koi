from django.db import models

class GroceryItem(models.Model):
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    created_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(null=True,default=False)
    
    def __str__(self):
        return self.item_name