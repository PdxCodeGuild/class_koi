from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:id>', views.detail),
    path('complete/<int:id>', views.complete),
    path('delete/<int:id>', views.delete),
    path('uncomplete/<int:id>', views.uncomplete),
]