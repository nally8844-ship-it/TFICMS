from rest_framework import viewsets, permissions
from .models import Consultation, Prescription
from .serializers import ConsultationSerializer, PrescriptionSerializer

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all().select_related('patient','doctor')
    serializer_class = ConsultationSerializer
    permission_classes = [permissions.IsAuthenticated]

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all().select_related('consultation')
    serializer_class = PrescriptionSerializer
    permission_classes = [permissions.IsAuthenticated]