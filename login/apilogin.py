from .models import CustomUser
from .serializers import RegisterSerializer
from rest_framework import viewsets, permissions

class loginViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer