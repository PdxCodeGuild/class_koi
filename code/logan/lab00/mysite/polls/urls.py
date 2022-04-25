from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]














# from django.urls import path

# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),

