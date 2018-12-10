# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import datetime
import time
import os

testMode = True

# initialize the camera and grab a reference to the raw camera capture
#~ resX = 3280
#~ resY = 2464
resX = 1648
resY = 1232
frameRate = 10
camera = PiCamera()
camera.resolution = (resX, resY)
camera.framerate = frameRate
rawCapture = PiRGBArray(camera, size=(resX, resY))
 
# allow the camera to warmup
time.sleep(0.1)

if not testMode:
	# Camera Consistency: https://picamera.readthedocs.io/en/release-1.13/recipes1.html
	camera.iso = 100
	# Wait for the automatic gain control to settle
	time.sleep(2)
	# Now fix the values
	camera.shutter_speed = camera.exposure_speed
	camera.exposure_mode = 'off'
	g = camera.awb_gains
	camera.awb_mode = 'off'
	camera.awb_gains = g
	camera.led = False
else:
	print "Warning, in test mode. Images not consistent."
 
font = cv2.FONT_HERSHEY_SIMPLEX

door1open = False
door2open = True
door3open = False
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
	
	key = cv2.waitKey(1) & 0xFF
	
	if key == ord("c"):
		cv2.imwrite("../capture {}.jpg".format(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')), image)
		
	 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
		
	if key == ord("p"):
		file = "kanye-west-power-intro.wav"
		os.system("omxplayer --no-keys {} &".format(file))

	# DO SAMPLING HERE
	
	# DO DRAWING HERE
	cv2.rectangle(image, (50, 50), (100, 100), (0, 255, 0), 1)
	
	cv2.putText(image, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),(10,500), font, 1,(255,255,255),2,cv2.CV_AA)
	cv2.putText(image, door1open and "door 1 open" or "door 1 closed",(10,500 + 50), font, 1,door1open and (0,255,0) or (0, 0, 255) ,2,cv2.CV_AA)
	cv2.putText(image, door2open and "door 2 open" or "door 2 closed",(10,500 + 100), font, 1,door2open and (0,255,0) or (0, 0, 255) ,2,cv2.CV_AA)
	cv2.putText(image, door3open and "door 3 open" or "door 3 closed",(10,500 + 150), font, 1,door3open and (0,255,0) or (0, 0, 255) ,2,cv2.CV_AA)
 
	# show the frame
	cv2.imshow("Frame", image)
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
