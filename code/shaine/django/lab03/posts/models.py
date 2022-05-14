from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Chirp(models.Model):
    text = models.CharField(max_length=128, default= '')
    datetime =  models.DateTimeField(default=timezone.now)
    uname = models.ForeignKey(User, on_delete=models.CASCADE)
