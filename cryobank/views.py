from rest_framework import viewsets, permissions
from .models import Cryotank, CryoStorageRecord, Donor
from .serializers import CryotankSerializer, CryoStorageRecordSerializer, DonorSerializer

class CryotankViewSet(viewsets.ModelViewSet):
    queryset = Cryotank.objects.all()
    serializer_class = CryotankSerializer
    permission_classes = [permissions.IsAuthenticated]

class CryoStorageRecordViewSet(viewsets.ModelViewSet):
    queryset = CryoStorageRecord.objects.all()
    serializer_class = CryoStorageRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

class DonorViewSet(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer
    permission_classes = [permissions.IsAuthenticated]