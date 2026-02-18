from rest_framework import serializers
from .models import Patient, CoupleProfile, PatientDocument, ConsentForm

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

class CoupleProfileSerializer(serializers.ModelSerializer):
    male_partner = PatientSerializer(read_only=True)
    female_partner = PatientSerializer(read_only=True)
    male_partner_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.filter(gender='male'), source='male_partner', write_only=True)
    female_partner_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.filter(gender='female'), source='female_partner', write_only=True)
    class Meta:
        model = CoupleProfile
        fields = "__all__"

class PatientDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDocument
        fields = "__all__"

class ConsentFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsentForm
        fields = "__all__"