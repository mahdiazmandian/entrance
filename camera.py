from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
for i in range(100):
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
camera.stop_preview()