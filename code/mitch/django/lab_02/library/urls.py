from django.urls import path, include

from . import views


app_name = "library"

urlpatterns = [
    path('', views.index, name='home'),
    path('author/<int:id>/', views.author, name='author'),
    path('book/<int:id>/', views.book, name='book'),

]









