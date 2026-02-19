from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    DEPARTMENT_CHOICES = (
        ('reception', '🎫 Front Office / Reception'),
        ('opd', '🏥 Outpatient Department (OPD)'),
        ('fertility_consultation', '🔍 Fertility Consultation Unit'),
        ('ivf', '🧬 IVF & ART Department'),
        ('andrology_lab', '🔬 Andrology Laboratory'),
        ('embryology_lab', '🥚 Embryology Laboratory'),
        ('ultrasound', '📡 Ultrasound & Imaging Department'),
        ('nursing', '   ‍⚕️ Nursing Department'),
        ('pharmacy', '💊 Pharmacy Department'),
        ('billing', '💰 Finance & Billing Department'),
        ('general_lab', '🧪 General Laboratory (Diagnostics)'),
        ('counseling', '💭 Counseling & Psychology Unit'),
        ('cryobank', '❄️ Cryobank Management'),
        ('hr', '👔 Human Resource (HR)'),
        ('admin', '⚙️ Administration & Management'),
    )
    
    department = models.CharField(
        max_length=50,
        choices=DEPARTMENT_CHOICES,
        default='reception'
    )
    phone = models.CharField(max_length=15, blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return f"{self.username} - {self.get_department_display()}"