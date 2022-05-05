from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('complete/<int:id>', views.complete),
    path('delete/<int:id>', views.delete),
    path('undo/<int:id>', views.undo),

]