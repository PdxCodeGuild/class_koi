from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self): 
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    checked_out = models.BooleanField(default=False)
    user = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['checked_out','-timestamp',]

    def __str__(self): 
        return self.title

    def set_checkout(self):
        self.checked_out = True
        self.timestamp = timezone.now()
        self.save()

    def set_checkin(self):
        self.checked_out = False
        self.timestamp = timezone.now()
        self.save()