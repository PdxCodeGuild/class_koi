from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:id>', views.detail),
    path('detail/<int:id>', views.detail),
    path('complete/<int:id>', views.complete),
    path('delete/<int:id>', views.delete),
    # path('', include('grocery_list.urls')),
]