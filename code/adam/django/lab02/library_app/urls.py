from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.detail, name='detail'),
    path('checkout/<int:id>', views.checkout, name='checkout'),
    path('checkin/<int:id>', views.checkin, name='checkin'),
]