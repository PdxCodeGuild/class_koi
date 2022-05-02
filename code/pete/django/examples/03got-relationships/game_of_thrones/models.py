from django.db import models

class House(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=40)
    # a ForeignKey is a One-to-Many relationship.
    # One house can have many characters.
    # Each character can only have one house
    house = models.ForeignKey(House, on_delete=models.PROTECT, related_name='characters')
    slug = models.SlugField()
    img_url = models.URLField(null=True, blank=True)

    # ManyToManyField is a many-to-many relationship
    # a character can have many houses that they are friendly with
    # a house can have many characters that it is friendly with
    # friendly_houses = models.ManyToManyField(House)

    # had to add related_name because there are 2 ManyToManyFields, each to the same Model
    # if you have just one ManyToManyField, or more than one, but they are to different Models,
    # you shouldn't have to add the related_name kwarg
    friends = models.ManyToManyField('Character', related_name='friendly_characters')
    enemies = models.ManyToManyField('Character', related_name='enemy_characters')

    def __str__(self):
        return self.name

