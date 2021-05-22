import os

from celery import Celery

_PROJECT_NAME = "cye"
_CELERY_PREFIX = 'CELERY'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery(_PROJECT_NAME)

app.config_from_object('django.conf:settings', namespace=_CELERY_PREFIX)

app.autodiscover_tasks()