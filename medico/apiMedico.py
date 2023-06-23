from .models import MedicoM
from rest_framework import viewsets, permissions
from .serializers import MedicoSerializer


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = MedicoM.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicoSerializer