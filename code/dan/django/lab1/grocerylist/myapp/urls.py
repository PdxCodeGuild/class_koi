from django.urls import path, include
from . import views
app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_item/', views.add_item),
    path('complete/', views.complete, name='complete'),
    path('delete/', views.delete),
]