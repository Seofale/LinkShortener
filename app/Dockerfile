FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app && apt-get update && apt-get install -y git libpq-dev postgresql-client
WORKDIR /app

COPY ./app/pyproject.toml /app/
COPY ./app/poetry.lock /app/

RUN pip install poetry && poetry config virtualenvs.create false && poetry install

COPY ./app /app
