import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tfirms.settings')

app = Celery('tfirms')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()