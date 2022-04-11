import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "send_email.settings")

app = Celery('send_email')
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-message-every-5-minute': {
        "task": "main.tasks.send_beat_email",
        "schedule": crontab(minute="*/5"),
    }
}

app.conf.broker_url = settings.REDIS_URL

app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'
