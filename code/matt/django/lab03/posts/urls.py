from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('boops/<str:author>/', views.user_feed, name='user_feed'),
    path('new/', views.add_post, name='new'),
    path('boops/<str:author>/<int:id>', views.post_detail, name='post_detail'),
]