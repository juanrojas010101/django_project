from rest_framework import routers
from .apiMedico import MedicoViewSet
from django.urls import path

router = routers.DefaultRouter()

router.register('apiMedico/MedicoM',MedicoViewSet, 'medico')


urlpatterns = router.urls