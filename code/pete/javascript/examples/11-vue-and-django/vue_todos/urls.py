from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('get-todos/', views.get_todos),
    path('add-todo/', views.add_todo),
]