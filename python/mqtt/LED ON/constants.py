from types import FunctionType


MQTT_SERVER = '333e9b6707ef4a7b9d22a69eb4d1a5c2.s1.eu.hivemq.cloud'
MQTT_PORT = 8883

TOPICS_TEST = 'esp_temp'
TOPICS_LED = "led"

MQTT_USER = "test1"
MQTT_PASS = "Password123456"

def ahoj():
    pass

print(type(ahoj) == FunctionType)