from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('user_checkout/', views.user_checkout),
    path('user_checkin/', views.user_checkin),
]