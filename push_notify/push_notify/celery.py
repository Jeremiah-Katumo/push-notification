
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'push_notify.settings')

app = Celery('push_notify')

app.config_from_object('django.conf:Settings', namespace='CELERY')

app.autodiscover_tasks()