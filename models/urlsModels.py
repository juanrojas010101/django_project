from rest_framework import routers
from .apiModels import ModelsViewSet
from django.urls import path

router = routers.DefaultRouter()

router.register('apiModels/Medico',ModelsViewSet, 'models')


urlpatterns = router.urls
