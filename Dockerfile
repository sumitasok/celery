FROM python:3.8.1

RUN pip install celery
RUN pip install psycopg2
RUN pip install sqlalchemy
RUN pip install celery[redis]
RUN pip install flower

WORKDIR /app
