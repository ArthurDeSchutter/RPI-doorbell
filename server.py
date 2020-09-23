from time import sleep
import picamera
from datetime import datetime
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
camera = picamera.PiCamera()

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.setup(12,GPIO.OUT)# led GPIO
GPIO.output(12,GPIO.LOW)#SET LED LOW

def button_callback(channel):
    
    print("Button was pushed!")
    record(10,getTime())


GPIO.add_event_detect(10,GPIO.FALLING,callback=button_callback) # Setup event on pin 10 rising edge


def record(time,filename):
    GPIO.output(12,GPIO.HIGH)
    
    filename = filename + ".h264"
    print(filename)
    camera.start_recording(filename)
    camera.wait_recording(int(time))
    camera.stop_recording()
    
    GPIO.output(12,GPIO.LOW)
    

def getTime():
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d_%m_%Y-%H_%M_%S")
    print(dt_string)
    return dt_string


