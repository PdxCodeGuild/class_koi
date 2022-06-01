from django.urls import path
from . import views

app_name = 'storied'
urlpatterns = [
    path('', views.index, name='index')
]

