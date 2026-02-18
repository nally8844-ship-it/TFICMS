from rest_framework import serializers
from .models import Drug, PrescriptionDispensing

class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = "__all__"

class PrescriptionDispensingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionDispensing
        fields = "__all__"