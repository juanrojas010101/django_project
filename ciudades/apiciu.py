from .models import Ciudad
from .serializers import CiudadSerializer
from rest_framework import viewsets, permissions

        
class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CiudadSerializer