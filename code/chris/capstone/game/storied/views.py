from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from storied.models import StoryTile
from storied.serializers import StoryTileSerializer

@api_view(['GET', 'POST'])
def story_tile_list(request, format=None):
    '''
    List all story tiles, or create a new story tile.
    '''

    if request.method == 'GET':
        story_tiles = StoryTile.objects.all()
        serializer = StoryTileSerializer(story_tiles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = StoryTileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def story_tile_detail(request, pk, format=None):
    '''
    Retrieve, update or delete a code snippet.
    '''
    try:
        story_tile = StoryTile.objects.get(pk=pk)
    except StoryTile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StoryTileSerializer(story_tile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StoryTileSerializer(story_tile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        story_tile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
