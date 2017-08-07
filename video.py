import time
from picamera import PiCamera
from datetime import datetime, timedelta

with PiCamera() as camera:
    camera.resolution = (1296, 730)
    camera.framerate = 15
    camera.start_preview()
    time.sleep(5)
    camera.zoom = (0.12,0.22,0.76,0.56)
    time.sleep(5)
    camera.zoom = (0.22,0.22,0.6,0.442)
    time.sleep(5)
    camera.zoom = (0.32,0.22,0.5,0.368)
    time.sleep(5)
