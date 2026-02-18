from django.db import models
from django.db import models
from django.conf import settings

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)

def patient_document_path(instance, filename):
    return f"patients/{instance.unique_id}/{filename}"

class Patient(models.Model):
    unique_id = models.CharField(max_length=20, unique=True, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='patients_created')
    emergency_contact = models.CharField(max_length=100, blank=True)
    referral_source = models.CharField(max_length=128, blank=True)

    def save(self, *args, **kwargs):
        if not self.unique_id:
            # Simple unique ID: PID + auto ID
            last_id = Patient.objects.all().order_by('-id').first()
            next_id = (last_id.id + 1) if last_id else 1
            self.unique_id = f"PID{next_id:06d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.unique_id} - {self.first_name} {self.last_name}"

class CoupleProfile(models.Model):
    male_partner = models.ForeignKey(Patient, related_name='male_couples', on_delete=models.CASCADE)
    female_partner = models.ForeignKey(Patient, related_name='female_couples', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Couple: {self.male_partner} + {self.female_partner}"

class PatientDocument(models.Model):
    patient = models.ForeignKey(Patient, related_name='documents', on_delete=models.CASCADE)
    file = models.FileField(upload_to=patient_document_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True)

class ConsentForm(models.Model):
    patient = models.ForeignKey(Patient, related_name='consent_forms', on_delete=models.CASCADE)
    file = models.FileField(upload_to=patient_document_path)
    form_type = models.CharField(max_length=64)
    date_signed = models.DateField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_withdrawn = models.BooleanField(default=False)