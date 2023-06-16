from .models import Soporte
from rest_framework import viewsets, permissions
from .serializers import SoporteSerializer

class SoporteViewSet(viewsets.ModelViewSet):
    queryset = Soporte.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SoporteSerializer