from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.authors, name='authors'),
    path('authors/<slug:slug>', views.author_detail, name='author_detail'),
    path('books/', views.books, name='books'),
    path('books/<slug:slug>', views.book_detail, name='book_detail'),
    path('history/', views.history, name='history'),
    path('genre/<slug:slug>', views.genre, name='genre'),
]