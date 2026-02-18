from django.db import models

class Drug(models.Model):
    name = models.CharField(max_length=128)
    batch_number = models.CharField(max_length=64)
    expiry_date = models.DateField()
    quantity_in_stock = models.PositiveIntegerField()
    controlled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (Batch: {self.batch_number})"

class PrescriptionDispensing(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    prescribed_by = models.CharField(max_length=128)
    prescribed_to = models.CharField(max_length=128)
    dispensed_on = models.DateField(auto_now_add=True)
    issued_by = models.CharField(max_length=128)
    note = models.TextField(blank=True)