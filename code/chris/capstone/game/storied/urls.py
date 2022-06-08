from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from storied import views

app_name = 'storied'
urlpatterns = [
    path('api_view/', views.story_tile_list),
    path('api_view/detail/<int:pk>', views.story_tile_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)