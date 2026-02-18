from django.db import models
from accounts.models import User

class AuditLog(models.Model):
    action = models.CharField(max_length=256)
    model = models.CharField(max_length=64)
    object_id = models.CharField(max_length=64)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    ip_addr = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    before = models.TextField(blank=True)
    after = models.TextField(blank=True)

    def __str__(self):
        return f"{self.timestamp} - {self.user} - {self.action} {self.model}:{self.object_id}"