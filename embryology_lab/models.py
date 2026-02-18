from django.db import models
from ivf.models import IVFCycle
from accounts.models import User

class Oocyte(models.Model):
    ivf_cycle = models.ForeignKey(IVFCycle, on_delete=models.CASCADE, related_name="oocytes")
    retrieval_date = models.DateField()
    number_retrieved = models.PositiveSmallIntegerField()
    mature = models.PositiveSmallIntegerField()
    comments = models.CharField(max_length=255, blank=True)
    witness = models.ForeignKey(User, related_name='oocyte_witness', on_delete=models.SET_NULL, null=True, blank=True)
    barcode = models.CharField(max_length=64, unique=True)

class Fertilization(models.Model):
    oocyte = models.ForeignKey(Oocyte, on_delete=models.CASCADE, related_name="fertilizations")
    date = models.DateField()
    method = models.CharField(max_length=64, choices=[("IVF","IVF"),("ICSI","ICSI")])
    fertilized = models.PositiveSmallIntegerField()
    normal = models.PositiveSmallIntegerField()
    abnormal = models.PositiveSmallIntegerField()
    comments = models.TextField(blank=True)

class Embryo(models.Model):
    ivf_cycle = models.ForeignKey(IVFCycle, on_delete=models.CASCADE, related_name="embryos")
    day = models.PositiveSmallIntegerField()  # D1-D6
    grade = models.CharField(max_length=16)
    biopsy_done = models.BooleanField(default=False)
    cryo_stored = models.BooleanField(default=False)
    witness = models.ForeignKey(User, related_name='embryo_witness', on_delete=models.SET_NULL, null=True, blank=True)
    barcode = models.CharField(max_length=64, unique=True)
    chain_of_custody = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)