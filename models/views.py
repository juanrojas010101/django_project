from django.shortcuts import render

from rest_framework.generics import DestroyAPIView
from models.models import Medico
from models.serializers import MedicoSerializer
from rest_framework.generics import DestroyAPIView


from rest_framework.generics import RetrieveUpdateAPIView



class EliminarMedico(DestroyAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    lookup_field = 'pk'

class ActualizarMedico(RetrieveUpdateAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    lookup_field = 'pk'

