# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import datetime
import time
 
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

	# DO SAMPLING HERE
	
	# DO DRAWING HERE
	cv2.rectangle(image, (50, 50), (100, 100), (0, 255, 0), 1)
 
	# show the frame
	cv2.imshow("Frame", image)
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)

		
	
