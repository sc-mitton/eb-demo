# Meant for a production environment

from celery import Celery
from celery.schedules import crontab

from django.apps import apps


# In production, make sure ssl is enabled
app = Celery("app")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.update(
    broker_connection_retry_on_startup=True,
    broker_connection_retry_interval=1,
)

app.conf.beat_schedule = {
    'fetch_investments_balance': {
        'task': 'app.tasks.dummy_beat',
        'schedule': crontab(hour=0, minute=0)
    },
}

app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])
