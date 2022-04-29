from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index),
    path('details/<int:id>/', views.details),
    path('checkouts/<int:id>/', views.checkouts)
]