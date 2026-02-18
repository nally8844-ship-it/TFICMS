from django import forms
from .models import Patient, CoupleProfile, PatientDocument, ConsentForm

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'gender', 'date_of_birth', 'phone', 'email', 'address', 'emergency_contact', 'referral_source']

class PatientDocumentForm(forms.ModelForm):
    class Meta:
        model = PatientDocument
        fields = ['file', 'description']

class ConsentFormForm(forms.ModelForm):
    class Meta:
        model = ConsentForm
        fields = ['file', 'form_type', 'date_signed']