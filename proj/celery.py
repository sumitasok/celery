from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

app = Celery('proj',
            # backend=os.environ['PG_CONN_STR'],
            # https://docs.celeryproject.org/en/latest/userguide/configuration.html#redis-backend-settings
            backend='redis://192.168.0.102:6379/0',
            broker=os.environ['CELERY_CONN_STR'],
            include=['proj.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
    task_track_started=True,
)

if __name__ == '__main__':
    app.start()