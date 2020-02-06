from celery import Celery
import os

app = Celery('tasks', broker=os.environ['CELERY_CONN_STR'])


@app.task
def add(x, y):
    return x + y
