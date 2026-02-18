from django.contrib import admin
from .models import Patient, CoupleProfile, PatientDocument, ConsentForm

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'first_name', 'last_name', 'gender', 'date_of_birth', 'phone', 'created_at')
    search_fields = ('unique_id', 'first_name', 'last_name', 'phone', 'email')

@admin.register(CoupleProfile)
class CoupleProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'male_partner', 'female_partner', 'created_at', 'is_active')

@admin.register(PatientDocument)
class PatientDocumentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'file', 'description', 'uploaded_at')

@admin.register(ConsentForm)
class ConsentFormAdmin(admin.ModelAdmin):
    list_display = ('patient', 'form_type', 'date_signed', 'uploaded_at', 'is_withdrawn')