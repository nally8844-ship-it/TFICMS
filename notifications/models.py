from django.db import models
from accounts.models import User

NOTIFICATION_TYPES = (
    ('sms','SMS'),
    ('email','Email'),
    ('both', 'SMS+Email')
)

class NotificationTemplate(models.Model):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=8, choices=NOTIFICATION_TYPES)
    subject = models.CharField(max_length=128, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.name

class NotificationLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    recipient = models.CharField(max_length=255)
    notification_type = models.CharField(max_length=8, choices=NOTIFICATION_TYPES)
    subject = models.CharField(max_length=128, blank=True)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=16, choices=(('sent','Sent'),('failed','Failed')), default='sent')
    response = models.CharField(max_length=512, blank=True)