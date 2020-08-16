import Adafruit_DHT
import ssl
import sys
import paho.mqtt.client as paho
import time
from time import sleep
from datetime import date, datetime

broker_address="192.168.1.200"
sensor = Adafruit_DHT.DHT22
pin = 4  # GPIO 21
delaySecondsBetweenPublish = 1
mqttClientId="IoTSensor"

mqtt = paho.Client(client_id="mqttClientId", clean_session=True)
mqtt.username_pw_set("testuser", "")
mqtt.connect("localhost", 1883, 30)

print("Subscribing to topic","house/bulbs/bulb1")
mqtt.subscribe("house/bulbs/bulb1")
print("Publishing message to topic","house/bulbs/bulb1")
mqtt.publish("house/bulbs/bulb1","OFF")


