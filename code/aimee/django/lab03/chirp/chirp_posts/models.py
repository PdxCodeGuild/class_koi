from django.db import models
from django.contrib.auth.models import User
# POSTS

#user as foreign key to posts
class Post(models.Model):
    description = models.CharField(max_length=50, blank=True)
    post_date = models.DateTimeField(auto_now=True, null=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.username}_{self.post_date}'


