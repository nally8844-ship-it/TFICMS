from rest_framework import viewsets, permissions
from .models import Patient, CoupleProfile, PatientDocument, ConsentForm
from .serializers import PatientSerializer, CoupleProfileSerializer, PatientDocumentSerializer, ConsentFormSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

class CoupleProfileViewSet(viewsets.ModelViewSet):
    queryset = CoupleProfile.objects.all()
    serializer_class = CoupleProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class PatientDocumentViewSet(viewsets.ModelViewSet):
    queryset = PatientDocument.objects.all()
    serializer_class = PatientDocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

class ConsentFormViewSet(viewsets.ModelViewSet):
    queryset = ConsentForm.objects.all()
    serializer_class = ConsentFormSerializer
    permission_classes = [permissions.IsAuthenticated]