# from rest_framework import routers
# from .apilogin import loginViewSet

# router = routers.DefaultRouter()

# router.register('apilogin/CustomUser',loginViewSet, 'apilogin')


# urlpatterns = router.urls
from .views import RegisterAPI
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    ]