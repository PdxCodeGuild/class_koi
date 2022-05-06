from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
path('', views.index, name='index'),
path('posts/world', views.world, name='world'),
path('posts/profile', views.profile, name='profile')
]