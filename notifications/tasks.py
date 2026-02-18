from celery import shared_task
from django.core.mail import send_mail
from .models import NotificationLog, NotificationTemplate
import requests, os

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID','')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN','')
TWILIO_NUMBER = os.getenv('TWILIO_FROM','')

@shared_task
def send_email_task(recipient, subject, body):
    try:
        send_mail(
            subject,
            body,
            os.getenv('DJANGO_DEFAULT_FROM_EMAIL','no-reply@tficms.local'),
            [recipient],
        )
        NotificationLog.objects.create(recipient=recipient, notification_type='email', subject=subject, body=body, status='sent')
        return True
    except Exception as e:
        NotificationLog.objects.create(recipient=recipient, notification_type='email', subject=subject, body=body, status='failed', response=str(e))
        return False

@shared_task
def send_sms_task(recipient, body):
    # Example with Twilio
    try:
        twilio_url = "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json".format(TWILIO_ACCOUNT_SID)
        data = {"From": TWILIO_NUMBER, "To": recipient, "Body": body}
        resp = requests.post(
            twilio_url,
            data=data,
            auth=(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        )
        NotificationLog.objects.create(recipient=recipient, notification_type='sms', body=body, status='sent', response=resp.text)
        return True
    except Exception as e:
        NotificationLog.objects.create(recipient=recipient, notification_type='sms', body=body, status='failed', response=str(e))
        return False