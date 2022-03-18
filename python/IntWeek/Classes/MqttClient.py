from types import FunctionType, MethodType
from config import Config

import paho.mqtt.client as mqtt

class MqttClient:
    def __init__(self, topic, callback = None, *vars) -> None:
        self.client = mqtt.Client(client_id="", userdata=None, protocol=mqtt.MQTTv5)
        self.__callback = callback
        self.__params = vars
        self.__topic = topic

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.client.username_pw_set(username=Config.MQTT_USER, password=Config.MQTT_PASS)
        self.client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

   # The callback for when the client receives a connect response from the server.
    def on_connect(self, client, userdata, flags, rc, idk):
        print("Connected with result code "+str(rc))
        print("Flags" + str(flags))

        # on_connect() means that if we lose the connection and reconnect then subscriptions will be renewed.
        client.subscribe(self.__topic)

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg: mqtt.MQTTMessage):
        print(msg.topic+" "+str(msg.payload))

        if type(self.__callback) == MethodType:
            self.__callback(msg.payload.decode())

    def connect(self) -> None:
        self.client.connect(Config.MQTT_SERVER, port=Config.MQTT_PORT, keepalive=60)
        self.client.loop_forever()