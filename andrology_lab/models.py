from django.db import models
from patients.models import Patient, CoupleProfile
from accounts.models import User

class SemenAnalysis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    volume_ml = models.DecimalField(max_digits=4, decimal_places=2)
    concentration_million_per_ml = models.DecimalField(max_digits=5, decimal_places=2)
    motility_percent = models.DecimalField(max_digits=5, decimal_places=2)
    morphology_percent = models.DecimalField(max_digits=5, decimal_places=2)
    comments = models.CharField(max_length=255, blank=True)
    analyst = models.ForeignKey(User, limit_choices_to={'role': 'andrology_tech'}, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} on {self.date} ({self.analyst})"

class SpermPreparation(models.Model):
    semen = models.ForeignKey(SemenAnalysis, related_name='preparations', on_delete=models.CASCADE)
    preparation_type = models.CharField(max_length=64, choices=[("swim-up","Swim Up"),("density","Density Gradient")])
    processed_by = models.ForeignKey(User, limit_choices_to={'role': 'andrology_tech'}, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    comments = models.CharField(max_length=255, blank=True)

class SpermFreezing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    straws_frozen = models.PositiveIntegerField()
    processed_by = models.ForeignKey(User, limit_choices_to={'role': 'andrology_tech'}, on_delete=models.SET_NULL, null=True)
    barcode = models.CharField(max_length=64, unique=True)
    thawed = models.BooleanField(default=False)
    thawed_on = models.DateField(null=True, blank=True)
    qc_check = models.CharField(max_length=255, blank=True)
    witness = models.ForeignKey(User, related_name='andrology_witness', limit_choices_to={'role': 'andrology_tech'}, on_delete=models.SET_NULL, null=True, blank=True)