from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='Posts', null=True)
    content = models.CharField(max_length=200)
    date_written = models.DateTimeField('date chirped', default=datetime.now)
    
    class Meta:
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return f'{self.author} tweet #{self.id}'
