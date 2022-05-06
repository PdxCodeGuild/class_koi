from django.db import models
from django.contrib.auth.models import User

class ChirpPost(models.Model):
    text = models.CharField(max_length=128)
    date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='chirp_posts')
    
    def __str__(self):
        return f'{self.user}@ {str(self.date_time)}: {self.text}'
