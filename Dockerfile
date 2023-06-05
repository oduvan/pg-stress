FROM python:3.11.2

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc libpq-dev postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt