import os
import shutil
from time import sleep
import picamera
from datetime import datetime
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import json
import pymongo

#mongoDB stuff
client = pymongo.MongoClient("mongodb+srv://APuser:Bulletbomb1@doorbellevents.xbdxu.mongodb.net/Events?retryWrites=true&w=majority")
db = client.test

#camera settings
camera = picamera.PiCamera()
camera.framerate = 15
#camera.resolution = (1920,1080)



GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.setup(12,GPIO.OUT)# led GPIO
GPIO.output(12,GPIO.LOW)#SET LED LOW

#set PIR sensor input
pir_pin = 17
GPIO.setup(pir_pin,GPIO.IN)
while True:
    if GPIO.input(PIR_PIN):
        print("Motion Detected!")
    time.sleep(1)


def button_callback(channel):
    JSONEvent = {
        "date": getTime(),
        "filename": getTime(),
        "photos":
        [
            "1" + getTime(),
            "2" + getTime(),
            "3" + getTime(),
        ]
        "favorite": False
    }
    print("Button was pushed!")
    record(10,JSONEvent.filename)
    #convert the dictionary in a proper JSON object
    JSONEvent = json.dumps(JSONEvent)
    db.Events.insert(JSONEvent)


GPIO.add_event_detect(10,GPIO.FALLING,callback=button_callback) # Setup event on pin 10 rising edge


def record(time,filename):
    GPIO.output(12,GPIO.HIGH)
    folder_Location = "/home/pi/Desktop/Windows-Share/"
    filename = folder_Location + filename + ".h264"
    print(filename)
    #capture image and start recording
    camera.capture("1" + filename, use_video_port=True)
    camera.start_recording(filename)
    #wait time / 2 to take a pic and start recording again
    camera.wait_recording(int(time/2))
    camera.capture("1" + filename, use_video_port=True)
    camera.wait_recording(int(time/2))
    #stop recording and capture final image
    camera.stop_recording()
    camera.capture("1" + filename, use_video_port=True)

    
    GPIO.output(12,GPIO.LOW)
    

def getTime():
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d_%m_%Y-%H_%M_%S")
    print(dt_string)
    return dt_string


#shutil.move("/home/pi/Documents/RPI-doorbell/MoveTest.txt", "DESKTOP-T2EQU5J/Users/Arthur%20De%20Schutter/Desktop/RPInetworkFolder")
