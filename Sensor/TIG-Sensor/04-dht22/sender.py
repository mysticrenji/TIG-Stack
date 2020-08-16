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
mqttClientId="dht22"
mqttPort=1883
mqttTopic_pub1 = "home/dht22/temperature"
mqttTopic_pub2 = "home/dht22/humidity"
mqttTopic_sub = "IoTSensor/Subscribe"
mqttTopic_state= "home/dht22/status"

#mqtt = paho.Client(client_id=mqttClientId, clean_session=True)
#mqtt.username_pw_set("testuser", "")
#mqtt.connect("localhost", 1883, 30)
#mqtt.publish("test", "test", qos=1, retain=True)
#print("Publishing message to topic","house/bulbs/bulb1")
#print("Subscribing to topic","house/bulbs/bulb1")

#mqtt.publish("house/bulbs/bulb1","OFF",qos=1,retain=True)

def on_connect(mqttc, obj, flags, rc):
    if rc == 0:
        print("Client conntected : " + str(rc) + " | Connection status: successful.")
        #mqttClient.subscribe(mqttTopic_sub, qos=1)
        mqttClient.publish(mqttTopic_state, "connected", 1, retain=True);
        publish_data()

def publish_data():
    time.sleep(delaySecondsBetweenPublish)
    now = datetime.utcnow()
    now_str = now.strftime('%Y-%m-%dT%H:%M:%SZ')
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        #payload = '{ "timestamp": "' + now_str + '","temperature": ' + str(result.temperature) + ',"humidity": '+ str(result.humidity": '+ str(result.humidity) '+'  }'
        #payload = '{{"timestamp":"{0}","humidity":{1:0.1f},"temperature":{2:0.1f}}}'.format(now_str,humidity,temperature)
        temp='"temperature":{0:0.1f}'.format(temperature)
        mqttClient.publish(mqttTopic_pub1, temp, 1,retain=True)
	    #print("Publish {0}".format(temp))
        humid='"humidity":{0:0.1f}'.format(humidity)
        mqttClient.publish(mqttTopic_pub2, humid, 1,retain=True)
       #print("Publish {0}".format(humidity))

def on_disconnect(client, userdata, rc):
    print("Client connection closed.")

def on_log(pahoClient, obj, level, string):
    print("---------------")
    print(string)

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))
    publish_data()

def teardown():
    mqttClient.disconnect()
    mqttClient.loop_stop()
    sys.exit()
#MQTT_USER = 'mqttuser'
#MQTT_PASSWORD = 'mqttpassword'
mqttClient = paho.Client(client_id=mqttClientId, clean_session=True)
mqttClient.username_pw_set("mqttuser", "mqttpassword")
mqttClient.on_connect = on_connect
mqttClient.on_disconnect = on_disconnect
mqttClient.on_publish = on_publish
mqttClient.on_log = on_log

print("Start connecting to " + broker_address + ":" + str(mqttPort) + " ...")

try:
    mqttClient.connect(broker_address, mqttPort)
    mqttClient.loop_forever()
except (KeyboardInterrupt, SystemExit):
    teardown()
