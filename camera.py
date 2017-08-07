#!/usr/bin/env python

from time import sleep
from time import time
import datetime
from picamera import PiCamera
from datetime import datetime, timedelta
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(13, GPIO.OUT)

#camera = PiCamera(resolution=(2592, 1944)) # For Rasberry Pi Camera v1 - 5Mp
camera = PiCamera(resolution=(3280, 2464)) # For Rasberry Pi Camera v2 - 8Mp
camera.start_preview()

def take_picture():
    GPIO.output(13,True)
    print datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S') + " taking image"
    imgFile = open('/mnt/img-' + datetime.fromtimestamp(time()).strftime('%Y%m%d %H%M%S') + '.jpg', 'wb')
    camera.capture(imgFile)
    imgFile.close()
    print datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S') + " done"
    GPIO.output(13,False)
    return;

# Capture test img on start. If capture fails, LED will stay ON signalling about issue.
take_picture()

while 1:
    if GPIO.input(7):
    	take_picture()

        while GPIO.input(7):
          sleep(0.5)

    sleep(0.5)
