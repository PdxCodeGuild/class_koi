from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>', views.delete),
    path('complete/<int:id>', views.complete),
    path('incomplete/<int:id>', views.incomplete)
]