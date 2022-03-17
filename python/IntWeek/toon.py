import RPi.GPIO as GPIO   #import the GPIO library
import time #import the time library
 
buzzer_pin = 12                  #set the buzzer pin variable to number 18
GPIO.setmode(GPIO.BOARD)#Use the Broadcom method for naming the GPIO pins
GPIO.setup(buzzer_pin, GPIO.OUT)  #Set pin 22 as an output pin
 
def buzz(pitch, duration):   #create the function "buzz" and feed it the pitch and duration)
 period = 1.0 / pitch     #in physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec)
 delay = period / 2     #calcuate the time for half of the wave
 cycles = int(duration * pitch)   #the number of waves to produce is the duration times the frequency
 
 for i in range(cycles):    #start a loop from 0 to the variable "cycles" calculated above
   GPIO.output(buzzer_pin, True)   #set pin 18 to high
   time.sleep(delay)    #wait with pin 18 high
   GPIO.output(buzzer_pin, False)    #set pin 18 to low
   time.sleep(delay)    #wait with pin 18 low
 
while True:    #start infinite loop
#   pitch_s = raw_input("Enter Pitch (200 to 2000): ")   #ask the user to type in the pitch
  pitch = float(pitch_s)    #convert user input to a floating decimal
#   duration_s = raw_input("Enter Duration (seconds): ")  #ask the user to type in the duration
  duration = float(duration_s)  #convert user input to a floating decimal
  buzz(pitch, duration)  #feed the pitch and duration to the function, "buzz"