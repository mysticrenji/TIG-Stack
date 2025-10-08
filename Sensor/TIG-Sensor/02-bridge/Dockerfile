FROM python:3.14-alpine

LABEL maintainer="Renji" \
      description="MQTT to InfluxDB Bridge"

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /app
WORKDIR /app

CMD ["python3", "-u", "main.py"]
