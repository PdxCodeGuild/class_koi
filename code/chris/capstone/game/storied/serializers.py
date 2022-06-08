from rest_framework import serializers
from storied.models import Story, StoryTile, CharacterPlayer

class StoryTileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryTile
        fields = ['id', 'x_coord', 'y_coord', 'prompt', 'enemy_tile', 'story']