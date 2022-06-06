from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('create/', views.CreateView.as_view(), name='create'),
    # path('<str:id>/glist.html', views.glist),
    path("<str:id>/complete/", views.complete, name="complete"),
    path("<str:id>/delete/", views.delete, name="delete"),
    path("<str:id>/glist", views.glist, name="glist"),
]
