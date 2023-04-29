from rest_framework import routers
from .apiespecialidad import EspecialidadViewSet

router = routers.DefaultRouter()

router.register('apiespecialidad/Especialidad',EspecialidadViewSet, 'apiespecialidad')


urlpatterns = router.urls
