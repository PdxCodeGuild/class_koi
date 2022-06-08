import datetime
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Story(models.Model):
    name = models.CharField(max_length=200)
    play_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Stories'

class StoryTile(models.Model):

    x_coord = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(4), MinValueValidator(0)])
    y_coord = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(4), MinValueValidator(0)])
    prompt = models.TextField()
    enemy_tile = models.BooleanField(default=False)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='Tiles')

    def __str__(self):
        tile_coords = (self.x_coord, self.y_coord)
        return f'{self.story} tile {tile_coords}'
class UserOptions(models.Model):

    move_fwd = 'FW'
    move_bwd = 'BW'
    move_lft = 'LF'
    move_rgt = 'RT'
    move_atk = 'AT'
    move_pkp = 'PU'
    USER_MOVES_CHOICES = [
        (move_fwd, 'Forward'),
        (move_bwd, 'Backward'),
        (move_lft, 'Left'),
        (move_rgt, 'Right'),
        (move_atk, 'Attack'),
        (move_pkp, 'Pick-up'),
    ]
    
    user_options = models.CharField(max_length=2, choices=USER_MOVES_CHOICES, null=True, blank=True)

class CharacterPlayer(models.Model):
    player_name = models.CharField(max_length=40)
    health_points = models.IntegerField()
