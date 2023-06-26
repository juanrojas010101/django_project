from rest_framework import routers
from .apiarchi import ArchivoViewSet

router = routers.DefaultRouter()

router.register('apiarchi/Archivo',ArchivoViewSet, 'archivos')


urlpatterns = router.urls