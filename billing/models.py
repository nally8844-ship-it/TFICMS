from django.db import models
from patients.models import Patient
from ivf.models import IVFCycle

class BillingPackage(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    ivf_cycle = models.ForeignKey(IVFCycle, on_delete=models.SET_NULL, null=True, blank=True)
    package = models.ForeignKey(BillingPackage, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    outstanding_balance = models.DecimalField(max_digits=12, decimal_places=2)
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    status = models.CharField(max_length=16, choices=[("open", "Open"), ("paid", "Paid"), ("overdue", "Overdue")], default="open")

    def __str__(self):
        return f"Invoice {self.id} - {self.patient} - {self.status}"

class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, related_name="payments", on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    mode = models.CharField(max_length=32, choices=[('cash', 'Cash'), ('mpesa', 'MPesa'), ('card', 'Card'), ('insurance', 'Insurance')], default='cash')
    notes = models.CharField(max_length=255, blank=True)