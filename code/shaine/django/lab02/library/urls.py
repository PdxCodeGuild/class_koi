from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='library-index'),
    path('check_out/<int:pk>/', views.check_out, name='library-check_out'),
    path('check_in/<int:pk>/', views.check_in, name='library-check_in'),
]
