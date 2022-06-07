from django.urls import include, path
from rest_framework import routers
from storied import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the borwsable API

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]



# app_name = 'storied'
# urlpatterns = [
#     path('', views.index, name='index')
# ]

