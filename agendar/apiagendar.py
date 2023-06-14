from .models import Agendar
from .serializers import AgendarSerializer
from rest_framework import viewsets, permissions

class AgendarViewSet(viewsets.ModelViewSet):
    queryset = Agendar.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AgendarSerializer