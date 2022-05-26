from django.urls import path,include
from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.addbook, name='addbook'),
    path('checkout',views.index, name='checkout')
]