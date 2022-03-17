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
        self.speaker = Speaker(12)
        self.speaker.setFreq(500)

        self.speaker.startPlaying()
        time.sleep(1)
        self.speaker.stopSound()

        print("Looping...")

    def loop(self):

        self.btn1.checkPresstimeOfButton(self.speaker.playTone, self.speaker.stopSound, (660,), ())
        self.btn2.checkPresstimeOfButton(self.speaker.playTone, self.speaker.stopSound, (880,), ())
        self.btn3.checkPresstimeOfButton(self.speaker.playTone, self.speaker.stopSound, (1100,), ())

        # self.play(self.btn1, self.speaker, 300)
        # play(self.btn2, self.speaker, 1000)
        # play(self.btn3, self.speaker, 1500)

    def stop(self):
        self.speaker.stopSound()


if __name__ == '__main__':
    try:
        main = Main()

        run = True
        while run:
            main.loop()
    except KeyboardInterrupt:
        main.stop()
