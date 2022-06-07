from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from storied.serializers import UserSerializer, GroupSerializer

from .models import StoryTile

class UserViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows users to be viewed or edited.
    '''
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows groups to be viewed or edited.
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializerpermission_classes = [permissions.IsAuthenticated]
# def index(request):
#     story_tiles = StoryTile.objects.all().values()

#     print(story_tiles)

#     context = {
#         'story_tiles': story_tiles,
#     }
#     return render(request, 'storied/index.html', context)