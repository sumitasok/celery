FROM python:3.8.1

RUN pip install celery
RUN pip install psycopg2
RUN pip install sqlalchemy

WORKDIR /app
