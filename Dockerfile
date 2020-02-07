FROM python:3.8.1

RUN pip install celery
RUN pip install psycopg2
RUN pip install sqlalchemy
# https://docs.celeryproject.org/en/latest/userguide/configuration.html#redis-backend-settings
RUN pip install celery[redis]
RUN pip install flower
# http://docs.celeryproject.org/en/latest/getting-started/next-steps.html#optimization
RUN pip install librabbitmq

WORKDIR /app
