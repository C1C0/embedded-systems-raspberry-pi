import RPi.GPIO as GPIO
import time

from gpiozero import Buzzer
from Classes.Device import Device

class Speaker(Device):
    def __init__(self, BPin, initFreq = 1000) -> None:
        GPIO.setup(BPin, GPIO.OUT)

        self.pin = BPin
        self.__freq = initFreq

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

    def playTone(self, freq:int):
        print("playing", freq)
        self.setFreq(freq)

        self.startPlaying()

    def testSpeaker(self):
        self.startPlaying()
        time.sleep(1)
        self.stopSound()

    def togglePlaying(self, freq):
        print("received freq: ", freq)

        if type(freq) == str:
            freq = int(freq)

        if freq > 0:
            self.playTone(freq)
        else:
            self.stopSound()

    def toon(self):
        pass
