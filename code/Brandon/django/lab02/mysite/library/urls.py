from django.urls import path, include
from django.contrib import admin

from . import views

app_name = 'library'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accounts/', include('accounts.urls')),
    # path('<int:id>/', views.book, name='book'),
    path('<int:id>/checkout/', views.checked_outs, name='checkout'),
    # path('<int:id>/checkout_book/', views.who_checked, name='who_checked_out'),
    path('<int:id>/checked_in/', views.checked_in, name='checked_in'),
]
