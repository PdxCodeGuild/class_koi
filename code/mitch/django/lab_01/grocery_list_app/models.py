from django.db import models
from django.utils import timezone

class GroceryItem(models.Model):
    description = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(null=True, blank=True) 
    completed = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.description
    
    
    
    
    
    
    