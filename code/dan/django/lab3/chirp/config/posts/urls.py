from django.urls import path
from . import views
from users.views import (
    register,
    login_view,
    logout
)


urlpatterns = [
    path('', views.index, name='home')
]