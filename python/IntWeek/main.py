# USING BOARD PINS

import threading
import time
import RPi.GPIO as GPIO

from config import Config
from Classes.Button import Button
from Classes.Speaker import Speaker
from Classes.MqttClient import MqttClient
from Classes.MqttPublisher import MqttPublisher

class Main():
    def __init__(self) -> None:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(True)

        self.__setup()

    def __setup(self):
        # Set buttons
        self.btn1 = Button(3)
        self.btn2 = Button(5)
        self.btn3 = Button(8)

        # Set speakers
        self.speaker1 = Speaker(12)
        self.speaker2 = Speaker(33)

        self.speaker1.testSpeaker()
        self.speaker2.testSpeaker()

        # Set subscribers
        self.mqttSub1 = MqttClient(Config.topics.SOUND_VIBORG)

        # Set publisher
        self.mqttPub1 = MqttPublisher(Config.MQTT_CLIENT_ID, (Config.topics.SOUND_GREENA, Config.topics.SOUND_SKIVE))

        # Start threading
        self.thMqttSound = threading.Thread(target=self.listenToOtherCampuses, args=(Config.topics.SOUND_VIBORG,))
        self.thMqttSound.start()

        print("Looping...")

    def loop(self):

        self.btn1.checkPresstimeOfButton(self.__playMe, self.speaker1.stopSound, (660,), ())
        self.btn2.checkPresstimeOfButton(self.speaker2.playTone, self.speaker2.stopSound, (880,), ())
        self.btn3.checkPresstimeOfButton(self.speaker1.playTone, self.speaker1.stopSound, (1100,), ())

    def stop(self):
        self.speaker1.stopSound()

    def __playMe(self, freq):
        self.mqttPub1.send(freq)
        self.speaker1.playTone(freq)

    def listenToOtherCampuses(self, topic):
        print("Starting Thread 2")
        # Set subscribers
        self.mqttSub1 = MqttClient(topic, print)
        self.mqttSub1.connect()


if __name__ == '__main__':
    try:
        main = Main()

        run = True
        while run:
            main.loop()
    except KeyboardInterrupt:
        main.stop()
