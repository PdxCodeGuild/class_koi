from django.urls import path
from django.contrib.auth.models import User
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.login, name='login'),
    path('', views.logout, name='logout'),
    path('', views.register, name='register'),
    path('', views.profile, name='profile'),
]