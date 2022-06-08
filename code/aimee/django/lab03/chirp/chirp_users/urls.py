from django.urls import path, include
from django.contrib import admin

from . import views
from chirp_posts.views import PostView, ProfileView


app_name = 'chirp_users'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', PostView.as_view(), name='index'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile')
]