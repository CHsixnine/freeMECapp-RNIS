import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json

class RNIS_MQTT_CLIENT():
    def __init__(self, BORKER_IP):
        self.client = mqtt.Client()
        self.BORKER_IP = BORKER_IP

    def send(self, payload, topic):
        publish.single(topic, json.dumps(payload), hostname=self.BORKER_IP)