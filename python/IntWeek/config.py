from types import FunctionType

class Config:
    MQTT_SERVER = '333e9b6707ef4a7b9d22a69eb4d1a5c2.s1.eu.hivemq.cloud'
    MQTT_PORT = 8883

    MQTT_USER = "test1"
    MQTT_PASS = "Password123456"

    MQTT_CLIENT_ID = 'Viborg'

    class topics:
        SOUND_VIBORG = 'sound-viborg'
        SOUND_SKIVE = 'sound-skive'
        SOUND_GREENA = 'sound-greena'