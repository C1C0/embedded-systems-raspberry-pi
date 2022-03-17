import RPi.GPIO as GPIO
import time

from Classes.Device import Device


class Button(Device):
    def __init__(self, BPin, initState=GPIO.HIGH, debounceDelay=60) -> None:
        super().__init__(BPin)

        print(f"BUTTON PIN: {self.pin}")

        self.__lastDebounceTimeMS = 0
        self.__lastButtonState = initState
        self.__debounceDelay = debounceDelay

        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def checkPresstimeOfButton(self, callback1, callback2, vars1: tuple, vars2: tuple) -> None:
        actualTime = round(time.time() * 1000)

        if actualTime > self.__lastDebounceTimeMS + self.__debounceDelay:
            self.__lastDebounceTimeMS = actualTime

            if GPIO.input(self.pin) != self.__lastButtonState:
                self.__lastButtonState = GPIO.input(self.pin)
                print("State", self.__lastButtonState)
                if self.__lastButtonState == GPIO.LOW:
                    callback1(*vars1)
                else:
                    callback2(*vars2)

    def getButtonState(self) -> bool:
        return self.__lastButtonState
