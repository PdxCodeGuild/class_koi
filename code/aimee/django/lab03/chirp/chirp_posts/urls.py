from django.urls import path, include
from django.contrib import admin

from . import views

app_name = 'chirp_posts'
urlpatterns = [
    path('post/', views.post_request, name="post"),
    
]