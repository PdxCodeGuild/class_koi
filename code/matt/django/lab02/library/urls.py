from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.authors, name='authors'),
    path('authors/<int:id>', views.author_detail, name='author_detail'),
    path('books/', views.books, name='books'),
    path('books/<int:id>', views.book_detail, name='book_detail'),
    path('history/', views.history, name='history'),
]