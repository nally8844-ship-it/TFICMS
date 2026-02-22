from django.contrib import admin
from .models import Department, Permission, DepartmentPermission, Patient, Appointment, Staff, Finance, Sample, LabResult, DepartmentReport

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'head', 'created_date']
    search_fields = ['name']

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ['permission', 'description']
    search_fields = ['permission']

@admin.register(DepartmentPermission)
class DepartmentPermissionAdmin(admin.ModelAdmin):
    list_display = ['department', 'permission']
    search_fields = ['department__name']
    list_filter = ['department']

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'age', 'status', 'registration_date']
    search_fields = ['name', 'email', 'phone']
    list_filter = ['status', 'gender', 'registration_date']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'department', 'doctor', 'appointment_date', 'status']
    search_fields = ['patient__name', 'doctor']
    list_filter = ['status', 'department', 'appointment_date']

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'role', 'department', 'status', 'joining_date']
    search_fields = ['name', 'email']
    list_filter = ['role', 'department', 'status']

@admin.register(Finance)
class FinanceAdmin(admin.ModelAdmin):
    list_display = ['reference_number', 'transaction_type', 'amount', 'department', 'patient', 'transaction_date']
    search_fields = ['reference_number', 'patient__name']
    list_filter = ['transaction_type', 'department', 'transaction_date']

@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ['sample_type', 'patient', 'department', 'collection_date', 'status']
    search_fields = ['patient__name', 'sample_type']
    list_filter = ['sample_type', 'department', 'status']

@admin.register(LabResult)
class LabResultAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'sample', 'date_tested', 'status']
    search_fields = ['test_name', 'sample__patient__name']
    list_filter = ['status', 'date_tested']

@admin.register(DepartmentReport)
class DepartmentReportAdmin(admin.ModelAdmin):
    list_display = ['department', 'total_appointments', 'completed_appointments', 'total_patients', 'revenue']
    list_filter = ['department', 'created_date']
