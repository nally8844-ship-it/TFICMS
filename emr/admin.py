from django.contrib import admin
from .models import Consultation, Prescription

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ['id','patient','doctor','date','diagnosis','icd_code']

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['id','consultation','medication','dosage','frequency','duration']