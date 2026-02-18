from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'doctor', 'scheduled_time', 'status', 'queue_number']
    list_filter = ['status', 'doctor', 'scheduled_time']