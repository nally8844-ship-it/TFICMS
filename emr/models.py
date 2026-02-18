from django.db import models
from django.conf import settings
from patients.models import Patient
from accounts.models import User

class Consultation(models.Model):
    patient = models.ForeignKey(Patient, related_name='consultations', on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name='doctor_consultations', on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField()
    diagnosis = models.CharField(max_length=256, blank=True)
    icd_code = models.CharField(max_length=16, blank=True)
    treatment_plan = models.TextField(blank=True)
    next_followup = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

class Prescription(models.Model):
    consultation = models.ForeignKey(Consultation, related_name='prescriptions', on_delete=models.CASCADE)
    medication = models.CharField(max_length=128)
    dosage = models.CharField(max_length=64)
    frequency = models.CharField(max_length=64)
    duration = models.CharField(max_length=64)
    instructions = models.TextField(blank=True)