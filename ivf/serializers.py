from rest_framework import serializers
from .models import IVFCycle, StimulationDay, EggRetrieval, EmbryoTransfer

class StimulationDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = StimulationDay
        fields = "__all__"

class EggRetrievalSerializer(serializers.ModelSerializer):
    class Meta:
        model = EggRetrieval
        fields = "__all__"

class EmbryoTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmbryoTransfer
        fields = "__all__"

class IVFCycleSerializer(serializers.ModelSerializer):
    stimulation_days = StimulationDaySerializer(many=True, read_only=True)
    egg_retrievals = EggRetrievalSerializer(many=True, read_only=True)
    embryo_transfers = EmbryoTransferSerializer(many=True, read_only=True)
    class Meta:
        model = IVFCycle
        fields = "__all__"