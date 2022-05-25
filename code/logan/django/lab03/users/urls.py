from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('user_login/', views.user_login, name="user_login"),
]