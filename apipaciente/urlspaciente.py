from rest_framework import routers
from .apipac import PacienteViewSet

router = routers.DefaultRouter()

router.register('apipac/Paciente',PacienteViewSet, 'apipaciente')


urlpatterns = router.urls

