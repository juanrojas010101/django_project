from django.shortcuts import render

from rest_framework.generics import DestroyAPIView
from models.models import Medico
from models.serializers import MedicoSerializer

class EliminarMedico(DestroyAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    lookup_field = 'pk'
