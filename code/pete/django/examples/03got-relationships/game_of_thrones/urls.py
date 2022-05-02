from django.urls import path

from . import views

app_name = 'thrones'
urlpatterns = [
    path('', views.index, name='home'),
    path('characters/<slug:slugified_name>/', views.character, name='character'),
    path('houses/<str:name>/', views.house, name='house'),
]