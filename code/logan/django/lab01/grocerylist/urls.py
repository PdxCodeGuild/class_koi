from django.urls import path
from . import views

app_name = 'grocerylist'
urlpatterns = [
    path('', views.index, name='index'),
    path("delete/<int:id>", views.delete, name="delete"),
    path("complete/<int:id>", views.complete, name="complete")
]



# index/