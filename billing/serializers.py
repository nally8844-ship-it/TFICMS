from rest_framework import serializers
from .models import BillingPackage, Invoice, Payment

class BillingPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingPackage
        fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

class InvoiceSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)
    class Meta:
        model = Invoice
        fields = "__all__"