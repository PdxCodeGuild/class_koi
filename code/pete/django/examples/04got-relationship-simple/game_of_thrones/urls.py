from django.urls import path

from . import views

app_name = 'thrones'
urlpatterns = [
    path('', views.index, name='home'),
    path('<str:name>/', views.house, name='house'),
]