from rest_framework import viewsets, permissions
from .models import BillingPackage, Invoice, Payment
from .serializers import BillingPackageSerializer, InvoiceSerializer, PaymentSerializer

class BillingPackageViewSet(viewsets.ModelViewSet):
    queryset = BillingPackage.objects.all()
    serializer_class = BillingPackageSerializer
    permission_classes = [permissions.IsAuthenticated]

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]