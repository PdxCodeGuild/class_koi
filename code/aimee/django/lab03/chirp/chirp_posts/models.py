from django.db import models
from django.contrib.auth.models import User
# POSTS

#user as foreign key to posts
class Post(models.Model):
    description = models.CharField(max_length=50, blank=True, null=False)
    post_date = models.DateTimeField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user}_{self.post_date}'


