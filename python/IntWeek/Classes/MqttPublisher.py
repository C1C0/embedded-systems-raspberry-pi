import paho.mqtt.client as mqtt
from config import Config

class MqttPublisher:
    def __init__(self, clientID, topics : tuple) -> None:
        self.client = mqtt.Client(client_id=clientID, userdata=None, protocol=mqtt.MQTTv5)
        self.__topics = topics

        self.sent = False

        self.client.on_publish = self.__on_publish
        
        self.client.username_pw_set(username=Config.MQTT_USER, password=Config.MQTT_PASS)
        self.client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

    def __on_publish(self, client, userdata, mid, properties=None):
        print("Data sent mid: " + str(mid))

    def send(self, payload):
        print("Sending: ", payload)
        self.client.connect(Config.MQTT_SERVER, Config.MQTT_PORT, 60)
        self.sent = True

        for topic in self.__topics:
            self.client.publish(topic, payload=payload, qos=1)

