from django.db import models

class ChirpPost(models.Model):
    #details of the post
    author = models.CharField(max_length=50)
    post_text = models.CharField(max_length=128)
    date_posted = models.DateField(auto_now_add=True)
    # date_edited = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.author}: {self.date_posted}'




