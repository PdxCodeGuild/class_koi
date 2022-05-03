from django.db import models

from states.models import State

class City(models.Model):
    climate_choices = [
        ('TR', 'Tropical'),
        ('DR', 'Dry'),
        ('TE', 'Temperate'),
        ('CT', 'Continental'),
        ('PO', 'Polar'),
    ]
    name = models.CharField(max_length=50)
    population = models.IntegerField()
    climate = models.CharField(max_length=2, choices=climate_choices)
    visited = models.BooleanField(default=False)

    state = models.ForeignKey(State, on_delete=models.PROTECT, null=True, blank=True)

    # this isn't necessary, just done so "Cities" appears correctly in the admin panel
    class Meta:
        verbose_name_plural = 'Cities'
    
    def __str__(self): # this determines how the object will appear when turned into a string
        # the default is ModelName (id) (City (1), City(2), etc.)
        # it is particularly helpful in the admin panel
        return self.name

# after creating or changing your models, run these 2 commands:
# py manage.py makemigrations
# py manage.py migrate

# to access the admin panel after migrating:
# py manage.py createsuperuser

# be sure to register your model in admin.py