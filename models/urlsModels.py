from rest_framework import routers
from .apiModels import ModelsViewSet

router = routers.DefaultRouter()

router.register('apiModels/Medico',ModelsViewSet, 'models')
router.register('apiModels/Paciente',ModelsViewSet, 'Paciente')

urlpatterns = router.urls
