from rest_framework import routers
from .apisop import SoporteViewSet
router = routers.DefaultRouter()

router.register('apisop/Soporte', SoporteViewSet, 'soporte' )


urlpatterns = router.urls