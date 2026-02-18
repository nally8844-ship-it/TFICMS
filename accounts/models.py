from django.contrib.auth.models import AbstractUser
from django.db import models

ROLES = [
    ('superadmin', 'Super Admin'),
    ('manager', 'Clinic Manager'),
    ('receptionist', 'Receptionist'),
    ('doctor', 'Doctor'),
    ('nurse', 'Nurse'),
    ('sonographer', 'Sonographer'),
    ('andrology_tech', 'Andrology Lab Technician'),
    ('embryology_tech', 'Embryology Lab Technician'),
    ('pharmacist', 'Pharmacist'),
    ('accountant', 'Accountant'),
    ('hr', 'HR Officer'),
    ('counselor', 'Counselor'),
    ('cryobank', 'Cryobank Officer'),
]

class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=32, choices=ROLES)
    phone = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"