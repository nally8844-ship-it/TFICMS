from rest_framework import viewsets, permissions
from .models import Drug, PrescriptionDispensing
from .serializers import DrugSerializer, PrescriptionDispensingSerializer

class DrugViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    permission_classes = [permissions.IsAuthenticated]

class PrescriptionDispensingViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionDispensing.objects.all()
    serializer_class = PrescriptionDispensingSerializer
    permission_classes = [permissions.IsAuthenticated]