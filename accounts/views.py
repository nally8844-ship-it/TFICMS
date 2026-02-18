from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, viewsets, permissions
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        # Set password here if coming from API
        user = serializer.save()
        raw_password = self.request.data.get('password')
        if raw_password:
            user.set_password(raw_password)
            user.save()