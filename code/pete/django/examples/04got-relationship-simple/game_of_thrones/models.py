from django.db import models

class House(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=40)
    house = models.ForeignKey(House, on_delete=models.PROTECT, related_name='characters')
    def __str__(self):
        return self.name

