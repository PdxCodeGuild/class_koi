from django.urls import path

from. import views

urlpatterns = [
    path('', views.index),
    path('<int:id>', views.detail),
    path('checkout/<int:id>', views.check_out),
    path('return/<int:id>', views.return_book),
]