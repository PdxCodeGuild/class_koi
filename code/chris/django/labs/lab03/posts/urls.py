from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='home'),
    path('chirps/<str:author>', views.profile, name='profile'),
]
