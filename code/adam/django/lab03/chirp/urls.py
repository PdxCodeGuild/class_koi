from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='home'),
    path('chirp/<int:id>/', views.detail, name='detail'),
]