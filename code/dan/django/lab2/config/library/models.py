from django.db import models
from django.utils import timezone
import datetime

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    author = models.ForeignKey('Author',on_delete=models.PROTECT, null=True)
    
    
class Checkinout(models.Model):
        title = models.CharField(max_length=200)
        name = models.CharField(max_length=200)
        lengthofcheckout = models.IntegerField(null=True)
        checkouttime = models.DateTimeField(default=timezone.now)
        in_out = models.BooleanField(null=True,default=False,)
        
def __str__(self):
    return self.myfield