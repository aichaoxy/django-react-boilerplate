FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /api

RUN pip install -r ../requirements.txt

COPY . .

EXPOSE 8000