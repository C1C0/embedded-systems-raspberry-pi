# USING BOARD PINS

import time
import RPi.GPIO as GPIO

from Classes.Button import Button
from Classes.Speaker import Speaker

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

        # Set speaker
        self.speaker1 = Speaker(12)
        self.speaker2 = Speaker(33)

        self.speaker1.testSpeaker()
        self.speaker2.testSpeaker()

        print("Looping...")

    def loop(self):

        self.btn1.checkPresstimeOfButton(self.speaker1.playTone, self.speaker1.stopSound, (660,), ())
        self.btn2.checkPresstimeOfButton(self.speaker2.playTone, self.speaker2.stopSound, (880,), ())
        self.btn3.checkPresstimeOfButton(self.speaker1.playTone, self.speaker1.stopSound, (1100,), ())

    def stop(self):
        self.speaker1.stopSound()


if __name__ == '__main__':
    try:
        main = Main()

        run = True
        while run:
            main.loop()
    except KeyboardInterrupt:
        main.stop()
