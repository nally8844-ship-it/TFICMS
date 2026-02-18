from rest_framework import viewsets, permissions
from .models import Oocyte, Fertilization, Embryo
from .serializers import OocyteSerializer, FertilizationSerializer, EmbryoSerializer

class OocyteViewSet(viewsets.ModelViewSet):
    queryset = Oocyte.objects.all()
    serializer_class = OocyteSerializer
    permission_classes = [permissions.IsAuthenticated]

class FertilizationViewSet(viewsets.ModelViewSet):
    queryset = Fertilization.objects.all()
    serializer_class = FertilizationSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmbryoViewSet(viewsets.ModelViewSet):
    queryset = Embryo.objects.all()
    serializer_class = EmbryoSerializer
    permission_classes = [permissions.IsAuthenticated]