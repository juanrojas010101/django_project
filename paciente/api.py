from .models import PacienteM
from .serializers import PacienteSerializer
from rest_framework import viewsets, permissions

        
class PacienteViewSet(viewsets.ModelViewSet):
    queryset = PacienteM.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PacienteSerializer