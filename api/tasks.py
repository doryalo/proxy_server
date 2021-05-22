import time

from celery import shared_task
from celery.utils.log import get_task_logger
import requests

logger = get_task_logger(__name__)


@shared_task(bind=True, track_started=True)
def get_users_list(self):
    res = requests.get('https://reqres.in/api/users?page=2')
    if res.status_code == 200:
        return res.json()