from django.db import models

# this will create a city table in the database
class City(models.Model):
    # models.CharField will create a field for entering strings into the database
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    # models.IntegerField will create a field for entering integers into the database
    population = models.IntegerField()
    food = models.CharField(max_length=50)
    mayor = models.CharField(max_length=50)
    climate = models.CharField(max_length=50)

    # by default, in the admin panel, the model will be shown as
    # model_name + 's', which gives us 'Citys' in this case
    # this right here is to override that to be 'Cities'
    class Meta:
        verbose_name_plural = 'cities'
    
    # without a __str__ method, these city objects will
    # just show up as City(1), City(2), etc.. when printed
    # as strings or in the admin panel, I'm adding the 
    # __str__ method here to show the city's name instead
    def __str__(self):
        return self.name