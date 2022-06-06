from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=25)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'ToDos' # was 'To dos' in admin panel before adding this
    
    def __str__(self):
        return self.text