from rest_framework import serializers
from .models import Cryotank, CryoStorageRecord, Donor

class CryotankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryotank
        fields = "__all__"

class CryoStorageRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryoStorageRecord
        fields = "__all__"

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = "__all__"