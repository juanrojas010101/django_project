from django.shortcuts import render

from rest_framework.generics import DestroyAPIView
from apipaciente.models import Paciente
from apipaciente.serializers import PacienteSerializer

from rest_framework.generics import RetrieveUpdateAPIView




class EliminarMiModelo(DestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    lookup_field = 'pk'

class ActualizarPaciente(RetrieveUpdateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    lookup_field = 'pk'

