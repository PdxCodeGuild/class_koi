from django.urls import path, include
from django.contrib import admin

from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index),
    path('details/<int:id>/', views.details),
    path('checkouts/<int:id>/', views.checkouts),
    path('records/', views.records)
]

# The current path, library/details/1/checkouts/1, didn’t match any of these. 