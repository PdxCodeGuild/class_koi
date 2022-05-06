from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='grocery-index'),
    path('update/<int:pk>/', views.update, name='grocery-update'),
    path('delete/<int:pk>/', views.delete, name='grocery-delete'),
]

