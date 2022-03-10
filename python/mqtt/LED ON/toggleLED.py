import RPi.GPIO as GPIO

LED_PIN = 2

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)

GPIO.output(LED_PIN, not GPIO.input(LED_PIN))