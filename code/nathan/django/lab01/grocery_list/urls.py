from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('add_grocery/', views.add_grocery),
    path('mark_complete/', views.mark_complete),
    path('delete_grocery/', views.delete_grocery)
]