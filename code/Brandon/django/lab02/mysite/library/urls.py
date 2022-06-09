from django.urls import path, include
from django.contrib import admin

from . import views

app_name = 'library'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('<int:id>', views.book, name='booklog'),
    path('checkout/<int:id>', views.checked_outs, name='checkout'),

    path('checked_in/<int:id>', views.checked_in, name='checkin'),
]
