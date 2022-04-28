from django.db import models

class GroceryItem(models.Model):
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    completed_date = models.CharField(max_length=200)
    iteam_boolean = models.BooleanField(max_length=200)
    
    def __str__(self):
        return self.myfield