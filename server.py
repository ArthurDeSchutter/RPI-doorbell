from time import sleep
from picamera import PiCamera
from datetime import datetime
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.setup(12,GPIO.OUT)# led GPIO
GPIO.output(12,GPIO.LOW)#SET LED LOW

def button_callback(channel):
    GPIO.output(12,GPIO.HIGH)
    print("Button was pushed!")
    sleep(1)
    GPIO.output(12,GPIO.LOW)

GPIO.add_event_detect(10,GPIO.FALLING,callback=button_callback) # Setup event on pin 10 rising edge


# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)


