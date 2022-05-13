from django.urls import path, include
from django.contrib import admin

from . import views

app_name = 'posts'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('users/', include('users.urls')),
]
