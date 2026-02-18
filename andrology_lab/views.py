from rest_framework import viewsets, permissions
from .models import SemenAnalysis, SpermPreparation, SpermFreezing
from .serializers import SemenAnalysisSerializer, SpermPreparationSerializer, SpermFreezingSerializer

class SemenAnalysisViewSet(viewsets.ModelViewSet):
    queryset = SemenAnalysis.objects.all()
    serializer_class = SemenAnalysisSerializer
    permission_classes = [permissions.IsAuthenticated]

class SpermPreparationViewSet(viewsets.ModelViewSet):
    queryset = SpermPreparation.objects.all()
    serializer_class = SpermPreparationSerializer
    permission_classes = [permissions.IsAuthenticated]

class SpermFreezingViewSet(viewsets.ModelViewSet):
    queryset = SpermFreezing.objects.all()
    serializer_class = SpermFreezingSerializer
    permission_classes = [permissions.IsAuthenticated]