from rest_framework import routers
from .api import PacienteViewSet

router = routers.DefaultRouter()

router.register('api/PacienteM',PacienteViewSet, 'paciente')


urlpatterns = router.urls