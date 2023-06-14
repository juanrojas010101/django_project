from rest_framework import routers
from .apiagendar import AgendarViewSet

router = routers.DefaultRouter()

router.register('apiagendar/Agendar',AgendarViewSet, 'agendar')


urlpatterns = router.urls