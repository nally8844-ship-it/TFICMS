from django.contrib import admin
from .models import Drug, PrescriptionDispensing

@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'batch_number', 'expiry_date', 'quantity_in_stock', 'controlled']
    search_fields = ['name', 'batch_number']

@admin.register(PrescriptionDispensing)
class DispenseAdmin(admin.ModelAdmin):
    list_display = ['id', 'drug', 'quantity', 'prescribed_by', 'prescribed_to', 'dispensed_on', 'issued_by']
    search_fields = ['prescribed_to']