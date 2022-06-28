from django.urls import path, include
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    path('author', views.author, name='author'),
    path('book', views.book, name='book'),
]