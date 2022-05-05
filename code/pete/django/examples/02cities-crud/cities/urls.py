from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),

    # this calls the view function like this:
    # detail(request, id=id)
    # where request is the HttpRequest
    # and id is the interger that was matched by '<int:id>'
    path('<int:id>', views.detail),

    path('visit/<int:id>', views.visit),
]