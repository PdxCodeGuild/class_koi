from django.db import models
from django.contrib.auth.models import User


class GroceryItem(models.Model):
    description = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)
    # null=True means the field can be NULL (None on in Python)
    # blank=True means the field doesn't have to be filled out in the admin panel
    completed_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField('bought', default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='grocery_items')
    
    def __str__(self):
        bought_status = 'bought' if self.completed else 'not bought'
        return f'{self.description}: {bought_status}'