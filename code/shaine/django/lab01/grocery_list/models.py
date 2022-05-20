from django.db import models
from django.utils import timezone


# Create your models here.
class Item(models.Model):
    content = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    date_completed = models.DateTimeField( null=True, blank=True)
    class Meta:
        ordering = ['complete','-date_created',]

    def __str__(self):
        return self.content


    # below to set complete time
    def set_complete(self):
        self.complete = True
        self.date_completed = timezone.now()
        self.save()

