from rest_framework import viewsets, permissions
from .models import IVFCycle, StimulationDay, EggRetrieval, EmbryoTransfer
from .serializers import (
    IVFCycleSerializer, StimulationDaySerializer, EggRetrievalSerializer, EmbryoTransferSerializer,
)

class IVFCycleViewSet(viewsets.ModelViewSet):
    queryset = IVFCycle.objects.all()
    serializer_class = IVFCycleSerializer
    permission_classes = [permissions.IsAuthenticated]

class StimulationDayViewSet(viewsets.ModelViewSet):
    queryset = StimulationDay.objects.all()
    serializer_class = StimulationDaySerializer
    permission_classes = [permissions.IsAuthenticated]

class EggRetrievalViewSet(viewsets.ModelViewSet):
    queryset = EggRetrieval.objects.all()
    serializer_class = EggRetrievalSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmbryoTransferViewSet(viewsets.ModelViewSet):
    queryset = EmbryoTransfer.objects.all()
    serializer_class = EmbryoTransferSerializer
    permission_classes = [permissions.IsAuthenticated]