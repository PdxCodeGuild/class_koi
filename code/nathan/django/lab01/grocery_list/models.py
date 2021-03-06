from django.db import models

# Create your models here.
class GroceryItem(models.Model):
    description = models.CharField(max_length = 250)
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField('date completed', null=True, blank=True)
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.description