FROM python:3.8.1

RUN pip install celery

WORKDIR /app
