from django.urls import path
from . import views

app_name = 'grocerylist'
urlpatterns = [
    path('', views.index, name='index'),
    path("delete/", views.delete, name="delete"),
    path("complete/", views.complete, name="complete")

]



# index/