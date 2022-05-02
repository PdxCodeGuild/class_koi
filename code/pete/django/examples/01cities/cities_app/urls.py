from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('cities/', views.cities),
    path('add-city/', views.add_city)
]