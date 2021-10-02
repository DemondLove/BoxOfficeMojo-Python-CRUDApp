#FROM ubuntu:20.04
FROM python:3.7.2-slim

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

ENTRYPOINT [ "flask", "run" ]

