from .models import Especialidad
from .serializers import EspecialidadSerializer
from rest_framework import viewsets, permissions

class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EspecialidadSerializer