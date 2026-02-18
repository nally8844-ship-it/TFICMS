from rest_framework import serializers
from .models import Oocyte, Fertilization, Embryo

class OocyteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oocyte
        fields = "__all__"

class FertilizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fertilization
        fields = "__all__"

class EmbryoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Embryo
        fields = "__all__"