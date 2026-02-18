from django.db import models
from patients.models import CoupleProfile, Patient
from accounts.models import User

CYCLE_STATUS = [
    ("registered", "Registered"),
    ("stimulation", "Ovarian Stimulation"),
    ("retrieval", "Egg Retrieval"),
    ("fertilization", "Fertilization"),
    ("transfer", "Embryo Transfer"),
    ("luteal_support", "Luteal Support"),
    ("pregnancy_test", "Pregnancy Test"),
    ("completed", "Completed"),
    ("cancelled", "Cancelled"),
]

PROTOCOLS = [
    ("long", "Long Protocol"),
    ("antagonist", "Antagonist"),
    ("minimal", "Minimal Stimulation"),
    ("natural", "Natural Cycle"),
]

class IVFCycle(models.Model):
    couple = models.ForeignKey(CoupleProfile, on_delete=models.CASCADE, related_name='ivf_cycles')
    registered_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    start_date = models.DateField()
    protocol = models.CharField(max_length=32, choices=PROTOCOLS)
    status = models.CharField(max_length=32, choices=CYCLE_STATUS, default='registered')
    notes = models.TextField(blank=True)
    outcome = models.CharField(max_length=256, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"IVF Cycle {self.pk} [{self.couple}] {self.status}"

class StimulationDay(models.Model):
    ivf_cycle = models.ForeignKey(IVFCycle, related_name='stimulation_days', on_delete=models.CASCADE)
    day_number = models.PositiveSmallIntegerField()
    date = models.DateField()
    estradiol = models.FloatField(null=True, blank=True)
    lh = models.FloatField(null=True, blank=True)
    progesterone = models.FloatField(null=True, blank=True)
    dominant_follicles = models.PositiveSmallIntegerField(null=True, blank=True)
    medication = models.CharField(max_length=128, blank=True)
    note = models.CharField(max_length=256, blank=True)

class EggRetrieval(models.Model):
    ivf_cycle = models.ForeignKey(IVFCycle, related_name='egg_retrievals', on_delete=models.CASCADE)
    date = models.DateField()
    eggs_collected = models.PositiveSmallIntegerField()
    matured_eggs = models.PositiveSmallIntegerField()
    comments = models.TextField(blank=True)

class EmbryoTransfer(models.Model):
    ivf_cycle = models.ForeignKey(IVFCycle, related_name='embryo_transfers', on_delete=models.CASCADE)
    date = models.DateField()
    embryos_transferred = models.PositiveSmallIntegerField()
    quality = models.CharField(max_length=128)
    outcome = models.CharField(max_length=128, blank=True)