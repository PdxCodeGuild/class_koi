from django.db import models

class Grocery(models.Model):
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    note = models.CharField(max_length=200, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    completed_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Groceries'

    def __str__(self):
        return self.item