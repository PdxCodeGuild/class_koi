from django.db import models

class State(models.Model):
    name = models.CharField(max_length=40)
    abbreviation = models.CharField(max_length=2)

    def __str__(self):
        return self.abbreviation