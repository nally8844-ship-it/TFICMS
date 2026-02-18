from django.db import models
from django.conf import settings
from patients.models import Patient
from accounts.models import User

APPOINTMENT_STATUS = [
    ("pending", "Pending"),
    ("confirmed", "Confirmed"),
    ("completed", "Completed"),
    ("cancelled", "Cancelled"),
    ("no_show", "No-show"),
]

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, related_name="appointments", on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, limit_choices_to={'role': 'doctor'}, related_name="doctor_appointments", on_delete=models.SET_NULL, null=True)
    scheduled_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=APPOINTMENT_STATUS, default="pending")
    queue_number = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    notes = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('scheduled_time', 'queue_number')

    def __str__(self):
        return f"{self.patient} with Dr.{self.doctor} at {self.scheduled_time.strftime('%Y-%m-%d %H:%M')} (Queue: {self.queue_number})"

from datetime import date

def next_queue_number(date_):
    # Counts existing appointments for a day and returns next queue number
    return 1 + Appointment.objects.filter(scheduled_time__date=date_).count()