
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'chirp'

urlpatterns = [
    path('', views.index, name='index'),
]


urlpatterns += staticfiles_urlpatterns()