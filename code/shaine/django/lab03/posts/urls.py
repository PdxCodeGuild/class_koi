from django.urls import path
from . import views
from .views import ChirpListView, ChirpCreateView, ChirpUpdateView, ChirpDeleteView

urlpatterns = [
    path('', ChirpListView.as_view(), name='index'),
    path('create/', ChirpCreateView.as_view(), name='chirpcreate'),
    path('chirp/<int:pk>/update', ChirpUpdateView.as_view(), name='chirpupdate'),
    path('chirp/<int:pk>/delete', ChirpDeleteView.as_view(), name='chirpdelete'),
]
