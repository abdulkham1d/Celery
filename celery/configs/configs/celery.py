import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')


app = Celery('configs')
app.config_from_object(f'django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()



app = Celery('configs')
app.conf.update(
    broker_connection_retry_on_startup=True,
    worker_pool_restarts=True,
    worker_concurrency=1,
)

app.conf.broker_url = 'redis://localhost:6379/0'  # Redis broker URL


# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')