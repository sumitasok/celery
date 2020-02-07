from celery import Celery
import os

app = Celery('tasks',
    backend=os.environ['PG_CONN_STR'],
    broker=os.environ['CELERY_CONN_STR'])

app.conf.update(
    task_serializer='json',
    # accept_content=['json'],  # Ignore other content
    # https://github.com/celery/celery/issues/3025
    # Always using Pickle for Postgres; SQLAlchemy can be altered to serialise before pickling.
    # should wait and watch if this issue is resolved; else have to consider another 
    result_serializer='json',
    timezone='Asia/Kolkata',
    # enable_utc=True,
)


@app.task
def add(x, y):
    return x + y
