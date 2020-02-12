from __future__ import absolute_import, unicode_literals

from .celery import app
from celery import Task
import time

# http://docs.celeryproject.org/en/latest/userguide/tasks.html#Task.autoretry_for
class BaseTaskWithRetry(Task):
    autoretry_for = (TypeError,)
    retry_kwargs = {'max_retries': 5}
    retry_backoff = True
    retry_backoff_max = 700
    retry_jitter = False

# default_retry_delay = 3 min (3*60) arg takes in sec.
@app.task(queue='add_task', name="proj.tasks.add", bind=True, max_retries=3, default_retry_delay=3*60,
            autoretry_for=(BrokenPipeError, ConnectionError,), retry_kwargs={'max_retries': 4}, # avoids need for try catch (try catch below for representation only).
            retry_backoff=True, # exponential back off to avoid overwhelming the services, adds random jitter.
            rate_limit='1/m', # 1/m means 1 per minute, /s, /h
            serializer='json', # http://docs.celeryproject.org/en/latest/userguide/tasks.html#Task.serializer
)
def add(self, x, y):
    try:
        return x + y
    except Exception as ex:
        raise self.retry(ex, countdown=12)

@app.task(acks_late=True)
def parrot(x):
    return x

@app.task
def delayed(n):
    time.sleep(n)

class DatabaseTask(Task):
    _db = None

    @property
    def db(self):
        if self._db is None:
            self._db = 0 #Database.connect()
        return self._db
# to use the same connection pool
@app.task(base=DatabaseTask)
def mul(x, y):
    return x * y

class XsumTask(Task):
    queue = 'xsum_task'

@app.task(base=XsumTask)
def xsum(numbers):
    return sum(numbers)