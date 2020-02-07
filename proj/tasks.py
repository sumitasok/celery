from __future__ import absolute_import, unicode_literals

from .celery import app
import time


@app.task
def add(x, y):
    return x + y

@app.task
def parrot(x):
    return x

@app.task
def delayed(n):
    time.sleep(n)


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)