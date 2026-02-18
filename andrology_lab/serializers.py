from rest_framework import serializers
from .models import SemenAnalysis, SpermPreparation, SpermFreezing

class SemenAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemenAnalysis
        fields = "__all__"

class SpermPreparationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpermPreparation
        fields = "__all__"

class SpermFreezingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpermFreezing
        fields = "__all__"