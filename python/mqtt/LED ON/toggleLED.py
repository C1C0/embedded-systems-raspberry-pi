import RPi.GPIO as GPIO
import time

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
        print(self.__lastButtonState)

        if actualTime > self.__lastDebounceTimeMS + self.__debounceDelay:
            self.__lastDebounceTimeMS = actualTime

            if GPIO.input(self.pin) != self.__lastButtonState:
                self.__lastButtonState = GPIO.input(self.pin)
                
                if self.__lastButtonState == GPIO.HIGH:
                    callback()

    def getButtonState(self) -> bool:
        return self.__lastButtonState

def setup() -> None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False) 

if __name__ == "__main__":
    setup()

    btn = Button(15)
    led = LED(2)

    while True:
        btn.checkPresstimeOfButton(led.toggle)