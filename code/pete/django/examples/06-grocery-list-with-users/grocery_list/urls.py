from django.urls import path

from . import views

app_name = 'groceries'
urlpatterns = [
    path('', views.index, name='home'),
    path('toggle-complete/<int:id>/', views.toggle_complete, name='toggle_complete'),
    path('delete/<int:id>/', views.delete, name='delete'),
]