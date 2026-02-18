from django import forms
from .models import Consultation, Prescription

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['patient', 'doctor', 'diagnosis', 'icd_code', 'notes', 'treatment_plan', 'next_followup']

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['medication','dosage','frequency','duration','instructions']