
#FROM python:3.7-alpine
FROM resin/rpi-raspbian:jessie
RUN apt-get update && \
    apt-get install -y \
      build-essential \
      bluez bluez-tools \
      python-dev python-pip \
      libglib2.0-dev libboost-python-dev libboost-thread-dev libbluetooth-dev && \
    pip install pybluez gattlib requests

LABEL maintainer="Renji" \
      description="MQTT to InfluxDB Bridge"


#RUN apk add --update-cache alpine-sdk build-base bluez


COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /app
WORKDIR /app

CMD ["python", "-u", "main.py"]
