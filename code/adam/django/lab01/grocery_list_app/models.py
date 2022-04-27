from django.db import models

# Create your models here.

class GroceryItem(models.Model):
    groceryitem_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')