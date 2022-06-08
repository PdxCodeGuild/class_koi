from django.db import models
from django.contrib.auth.models import User

from PIL import Image

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')
    timestamp = models.DateTimeField(blank=True)
    text_content = models.CharField(max_length=256, blank=True, default='')
    image_content = models.ImageField(upload_to='image_content/', blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image_content:
            img = Image.open(self.image_content.path)
            height, width = img.size
            max_dim = 1200
            if height > max_dim or width > max_dim:
                if height > width:
                    ratio = height / max_dim
                    height = max_dim
                    width = int(width / ratio)
                else:
                    ratio = width / max_dim
                    width = max_dim
                    height = int(height / ratio)
            img = img.resize((height, width))
            img.save(self.image_content.path, "JPEG", quality=99)

    def __str__(self):
        return f'{self.author}_{str(self.id)}'