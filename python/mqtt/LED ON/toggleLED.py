from ast import arg
from cgitb import enable
from types import FunctionType
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import constants as C
import threading

class MQTTC:
    def __init__(self, topic, callback = '', parameters = '') -> None:
        self.client = mqtt.Client(client_id="", userdata=None, protocol=mqtt.MQTTv5)
        self.__callback = callback
        self.__params = parameters
        self.__topic = topic

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.client.username_pw_set(username=C.MQTT_USER, password=C.MQTT_PASS)
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

        if type(self.__callback) == FunctionType:
            self.__callback(msg.payload.decode(), self.__params)

    def connect(self) -> None:
        self.client.connect(C.MQTT_SERVER, port=C.MQTT_PORT, keepalive=60)
        self.client.loop_forever()

class Device:
    def __init__(self, BCMPin) -> None:
        self.pin = BCMPin

class LED(Device):
    def __init__(self, BCMPin, initState = GPIO.LOW) -> None:
        super().__init__(BCMPin)

        self.__state = initState

        print(f"LED PIN: {self.pin}")

        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, self.__state) 

    def toggle(self) -> None:   
        self.__state = not self.__state 
        GPIO.output(self.pin, self.__state)

    def on(self) -> None:
        self.__state = GPIO.HIGH 
        GPIO.output(self.pin, self.__state)

    def off(self) -> None:
        self.__state = GPIO.LOW 
        GPIO.output(self.pin, self.__state)

class Button(Device):
    def __init__(self, BCMPin, initState = GPIO.LOW, debounceDelay = 60) -> None:
        super().__init__(BCMPin)

        print(f"BUTTON PIN: {self.pin}")

        self.__lastDebounceTimeMS = 0
        self.__lastButtonState = initState 
        self.__debounceDelay = debounceDelay

        GPIO.setup(self.pin, GPIO.IN) 

    def checkPresstimeOfButton(self, callback) -> None:
        actualTime = round(time.time() * 1000)

        if actualTime > self.__lastDebounceTimeMS + self.__debounceDelay:
            self.__lastDebounceTimeMS = actualTime

            if GPIO.input(self.pin) != self.__lastButtonState:
                self.__lastButtonState = GPIO.input(self.pin)
                
                if self.__lastButtonState == GPIO.HIGH:
                    callback()

    def getButtonState(self) -> bool:
        return self.__lastButtonState

def checkMqttSwitch(msg, params) -> None:
    print(msg)
    if msg == "ON":
        params[0].on()
        
    if msg == "OFF":
        params[0].off()

def setup() -> None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False) 

def enableMQtt(led :LED):
    mqttClient = MQTTC(C.TOPICS_LED, checkMqttSwitch, [led])
    mqttClient.connect()

def measureTmpMQtt():
    mqttClient = MQTTC(C.TOPICS_TEST)
    mqttClient.connect()

if __name__ == "__main__":
    setup()

    btn = Button(15)
    led = LED(2)

    thMqttLED = threading.Thread(target=enableMQtt, args=(led, ))
    thMqttLED.start()

    thMqttTemp = threading.Thread(target=measureTmpMQtt, args=())
    thMqttTemp.start()

    while True:
        btn.checkPresstimeOfButton(led.toggle)
    