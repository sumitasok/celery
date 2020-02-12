from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

app = Celery('proj',
            # backend=os.environ['PG_CONN_STR'],
            # https://docs.celeryproject.org/en/latest/userguide/configuration.html#redis-backend-settings
            backend=os.environ['REDIS_BACKEND'],
            broker=os.environ['CELERY_CONN_STR'],
            include=['proj.tasks'])

CELERY_ROUTES = {
    'core.tasks.xsum': {'queue': 'too_long_queue'},
    'core.tasks.add': {'queue': 'quick_queue'},
}

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
    task_track_started=True,
)

if __name__ == '__main__':
    app.start()