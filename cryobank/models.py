from django.db import models
from patients.models import Patient
from accounts.models import User

SPECIMEN_TYPE = [("embryo", "Embryo"), ("sperm", "Sperm"), ("oocyte", "Oocyte")]

class Cryotank(models.Model):
    name = models.CharField(max_length=64)
    capacity = models.PositiveIntegerField()
    location = models.CharField(max_length=64)
    temperature = models.FloatField(default=-196.0)  # Liquid nitrogen
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

class CryoStorageRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    specimen_type = models.CharField(max_length=16, choices=SPECIMEN_TYPE)
    tank = models.ForeignKey(Cryotank, on_delete=models.CASCADE)
    canister = models.CharField(max_length=32)
    goblet = models.CharField(max_length=32)
    straw = models.CharField(max_length=32)
    barcode = models.CharField(max_length=64, unique=True)
    stored_on = models.DateField(auto_now_add=True)
    withdrawn_on = models.DateField(null=True, blank=True)
    consent_form = models.FileField(upload_to="cryobank/consent/", blank=True, null=True)
    witness = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    storage_billing_due = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.patient}-{self.specimen_type}-{self.barcode}"

class Donor(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=32, unique=True)
    donor_type = models.CharField(max_length=16, choices=[('sperm','Sperm'),('egg','Egg'),('embryo','Embryo')])
    notes = models.TextField(blank=True)
    active = models.BooleanField(default=True)