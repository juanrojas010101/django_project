from rest_framework import routers
from .apiciu import CiudadViewSet

router = routers.DefaultRouter()

router.register('apiciu/Ciudad',CiudadViewSet, 'ciudades')


urlpatterns = router.urls