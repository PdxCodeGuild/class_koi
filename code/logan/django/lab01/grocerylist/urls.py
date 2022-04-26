from django.urls import path
from . import views

app_name = 'grocerylist'
urlpatterns = [
    path('index/', views.index, name='index')
]