import RPi.GPIO as GPIO
import time

from gpiozero import Buzzer
from Classes.Device import Device

class Speaker(Device):
    def __init__(self, BPin) -> None:
        GPIO.setup(BPin, GPIO.OUT)

        self.pin = BPin
        self.__freq = 1000

        self.__setSpeaker()

    def __setSpeaker(self):
        self.speaker = GPIO.PWM(self.pin, self.__freq)
        self.speaker.start(20)

    def startPlaying(self):
        # if GPIO.input(self.pin) != GPIO.HIGH:
        self.speaker.start(20)
        GPIO.output(self.pin, GPIO.HIGH)
        
    def stopSound(self):
        print("stopping")
        self.speaker.stop()

    def setFreq(self, freq):
        self.__freq = freq
        self.speaker.ChangeFrequency(freq)

    def playTone(self, freq):
        print("playing", freq)
        self.setFreq(freq)

        self.startPlaying()

    def toon(self):
        pass
