# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

ENV FLASK_APP=app.py

RUN mkdir /app

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py app.py
COPY MemoryClasses.py MemoryClasses.py
COPY static static
COPY templates templates

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5002"]
