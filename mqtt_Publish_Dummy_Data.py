# ------------------------------------------
# --- Author: Pradeep Singh
# --- Date: 20th January 2017
# --- Version: 1.0
# --- Python Ver: 2.7
# --- Details At: https://iotbytes.wordpress.com/store-mqtt-data-from-sensors-into-sql-database/
# ------------------------------------------


import paho.mqtt.client as mqtt
import random
import threading
import json
from datetime import datetime

# ====================================================
# MQTT Settings
MQTT_Broker = "iot.eclipse.org"
# MQTT_Broker = "localhost"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic_Sensor = "Home/Sensors/Motion"
# MQTT_Topic_Humidity = "Home/BedRoom/DHT22/Humidity"
MQTT_Topic_Temperature = "Home/Sensors/Temperature"

# ====================================================


def on_connect(client, userdata, rc):
    if rc != 0:
        pass
        print("Unable to connect to MQTT Broker...")
    else:
        print("Connected with MQTT Broker: " + str(MQTT_Broker))


def on_publish(client, userdata, mid):
    pass


def on_disconnect(client, userdata, rc):
    if rc != 0:
        pass


mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))


def publish_To_Topic(topic, message):
    mqttc.publish(topic, message)
    print("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic))
    print("")


# ====================================================
# FAKE SENSOR
# Dummy code used as Fake Sensor to publish some random values
# to MQTT Broker

toggle = 0


def publish_Fake_Sensor_Values_to_MQTT():
    threading.Timer(3.0, publish_Fake_Sensor_Values_to_MQTT).start()
    global toggle
    togglenum = int(random.uniform(0, 5))
    if toggle == 0:
        Motion_Fake_Value = int(random.uniform(0, 2))

        Motion_Data = {}
        Motion_Data['Sensor_ID'] = "Bed-1"
        Motion_Data['Date'] = (datetime.today()).strftime(
            "%d-%b-%Y %H:%M:%S:%f")
        Motion_Data['Motion'] = Motion_Fake_Value
        Motion_json_data = json.dumps(Motion_Data)

        print("Publishing Sensor Value: " +
              str(Motion_Fake_Value) + "...")
        publish_To_Topic(MQTT_Topic_Sensor, Motion_json_data)
        toggle = togglenum

    else:
        Motion_Fake_Value = int(random.uniform(0, 2))

        Motion_Data = {}
        Motion_Data['Sensor_ID'] = "Corridor-1"
        Motion_Data['Date'] = (datetime.today()).strftime(
            "%d-%b-%Y %H:%M:%S:%f")
        Motion_Data['Motion'] = Motion_Fake_Value
        Motion_json_data = json.dumps(Motion_Data)

        print("Publishing Sensor Value: " +
              str(Motion_Fake_Value) + "...")
        publish_To_Topic(MQTT_Topic_Sensor, Motion_json_data)
        toggle = togglenum


publish_Fake_Sensor_Values_to_MQTT()

# ====================================================
