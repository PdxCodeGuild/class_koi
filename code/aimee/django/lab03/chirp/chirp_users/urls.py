from django.urls import path, include
from django.contrib import admin

from . import views

app_name = 'chirp_users'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
]