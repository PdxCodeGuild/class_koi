from django.urls import path
from django.conf.urls.static import static
from config import settings

from . import views

app_name = 'nutrition'
urlpatterns = [
    path('', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)