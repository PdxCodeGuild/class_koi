from django.db import models
from django.contrib.auth.models import User

from PIL import Image

class Post(models.Model):
    username = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    text_content = models.CharField(max_length=256, blank=True, default='')
    image_content = models.ImageField(upload_to='image_content/', blank=True)

    # def save(self):
    #     if self.image_content:
    #         self.image_content = self.image_content.resize((1000, 1000))

    def __str__(self):
        return f'{self.username}_{str(self.id)}'


'''
x-user
x-datetime
x-text (constrained to ??? chars)
x-image (optional)

heart/like ???
tagging ???
post only to profile bool ???
replies ???
pinned post ???

DM ???
'''