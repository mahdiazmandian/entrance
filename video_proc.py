# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import datetime
import time
import os
import numpy as np
import math
import colorsys
from fractions import Fraction

testMode = False

showCalibration = False



######################################################### COPIED FROM GEANYTEST
img = np.zeros((1,1,3), np.uint8)

dummy_img = np.zeros((1,1,3), np.uint8)

door1MidX = 190
door1MidY = 436
box1X = 10
box1Y = 15

door2MidX = 964
door2MidY = 561
box2X = 8
box2Y = 15

door3MidX = 1381
door3MidY = 582
box3X = 5
box3Y = 15

col_open1 = (0, 0, 0)
col_open2 = (0, 0, 0)
col_open3 = (0, 0, 0)
col_close1 = (0, 0, 0)
col_close2 = (0, 0, 0)
col_close3 = (0, 0, 0)

def get_door_ref_colors(door_num, midX, midY, boxX, boxY):
        filename = ''
        
        if door_num == 1:
                filename = 'door1_open.jpg'
        elif door_num == 2:
                filename = 'door2_open.jpg'
        else:
                filename = 'door3_open.jpg'
                
        openR, openG, openB = getAverageColorOfBox(filename, dummy_img, midX, midY, boxX, boxY)
        closeR, closeG, closeB = getAverageColorOfBox('doors_closed.jpg', dummy_img, midX, midY, boxX, boxY)
        print 'average open: {}, {}, {}'.format(openR, openG, openB)
        print 'average close: {}, {}, {}'.format(closeR, closeG, closeB)

        #~ testR, testG, testB = getAverageColorOfBox('test_open.jpg', 303, 52)
        #~ testR, testG, testB = getAverageColorOfBox('test_closed.jpg', 303, 52)
        #~ print 'average test: {}, {}, {}'.format(testR, testG, testB)

        #~ openDist = getColorDist(testR, testG, testB, openR, openG, openB)
        #~ closeDist = getColorDist(testR, testG, testB, closeR, closeG, closeB)
        #~ print 'open dist: {}'.format(openDist)
        #~ print 'close dist: {}'.format(closeDist)
        #~ if openDist < closeDist:
                #~ print 'door is open'
        #~ else:
                #~ print 'door is closed'
        return (openR, openG, openB), (closeR, closeG, closeB)

def check_door_open(door_num, img):
	# using BGR format
	midX = 0
	midY = 0
	boxX = 0
	boxY = 0
	openC = (0, 0, 0)
	closeC = (0, 0, 0)
	if door_num == 1:
			midX = door1MidX
			midY = door1MidY
			boxX = box1X
			boxY = box1Y
			openC = col_open1
			closeC = col_close1
	elif door_num == 2:
			midX = door2MidX
			midY = door2MidY
			boxX = box2X
			boxY = box2Y
			openC = col_open2
			closeC = col_close2
	elif door_num == 3:
			midX = door3MidX
			midY = door3MidY
			boxX = box3X
			boxY = box3Y
			openC = col_open3
			closeC = col_close3
	
	currR, currG, currB = getAverageColorOfBox('', img, midX, midY, boxX, boxY)
	print "Door {}".format(door_num)
	print "Open: ({}, {}, {})".format(openC[0], openC[1], openC[2])
	print "Close: ({}, {}, {})".format(closeC[0], closeC[1], closeC[2])
	print "Curr: ({}, {}, {})".format(currR, currG, currB)
	
	#~ openH = colorsys.rgb_to_hls(openC[2]/255, openC[1]/255, openC[0]/255)
	#~ closeH = colorsys.rgb_to_hls(closeC[2]/255, closeC[1]/255, closeC[0]/255)
	#~ currH = colorsys.rgb_to_hls(currB/255, currG/255, currR/255)
	
	openH = colorsys.rgb_to_hls(openC[2]/255.0, openC[1]/255.0, openC[0]/255.0)[0]
	closeH = colorsys.rgb_to_hls(closeC[2]/255.0, closeC[1]/255.0, closeC[0]/255.0)[0]
	currH = colorsys.rgb_to_hls(currB/255.0, currG/255.0, currR/255.0)[0]
	
	#~ print 
	
	print "OpenH: {}".format(openH)
	print "CloseH: {}".format(closeH)
	print "CurrH: {}".format(currH)
	
	openDist = abs(openH - currH)
	closeDist = abs(closeH - currH)
	
	#~ openDist = 0
	#~ closeDist = 0
	
	#~ openDist = getColorDist(currR, currG, currB, openC[0], openC[1], openC[2])
	#~ closeDist = getColorDist(currR, currG, currB, closeC[0], closeC[1], closeC[2],)
    #~ print 'open dist: {}'.format(openDist)
    #~ print 'close dist: {}'.format(closeDist)
    #~ print 'open dist: {}'.format(openDist)
    #~ print 'close dist: {}'.format(closeDist)
	#~ if openDist < closeDist:
		#~ print 'door is open'
	#~ else:
		#~ print 'door is closed'
	return openDist < closeDist
	

def getAverageColorOfBox(fileName, img, x, y, searchBoxX, searchBoxY):
        if not fileName == '':
                img = cv2.imread(fileName)
        sumR = 0
        sumG = 0
        sumB = 0

        for pixelX in range(x - searchBoxX, x + searchBoxX + 1):
                for pixelY in range(y - searchBoxY, y + searchBoxY + 1):
                        sumR += img[pixelY, pixelX, 0]
                        sumG += img[pixelY, pixelX, 1]
                        sumB += img[pixelY, pixelX, 2]
                        #~ print img[y, x, 0], img[y, x, 1], img[y, x, 2]
        factor = (2 * searchBoxX + 1)  * (2 * searchBoxY + 1)
        sumR /= factor
        sumG /= factor
        sumB /= factor
        
        #~ print sumR, sumG, sumB
        
        cv2.rectangle(img, (x - searchBoxX, y - searchBoxY), (x + searchBoxX, y + searchBoxY), (0, 255, 0), 1)
        if showCalibration:
			cv2.namedWindow('image')
			cv2.setMouseCallback('image',draw_circle)
			cv2.imshow('image',img)
			cv2.waitKey(0)
			cv2.destroyAllWindows()
        return sumR, sumG, sumB

def getColorDist(r0, g0, b0, r1, g1, b1):
        return math.sqrt((r0 - r1)**2 + (g0 - g1)**2 + (b0 - b1)**2)
########################################################################### END OF GEANYTEST

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        #~ cv.circle(img,(x,y),100,(255,0,0),-1)
        print 'clicked: ({}, {})'.format(x, y)



# initialize the camera and grab a reference to the raw camera capture
#~ resX = 3280
#~ resY = 2464
resX = 1648
resY = 1232
#~ resX = 640
#~ resY = 480
frameRate = 3
camera = PiCamera()
camera.resolution = (resX, resY)
camera.framerate = frameRate
rawCapture = PiRGBArray(camera, size=(resX, resY))

# PERFORM COLOR LOOKUPS
col_open1, col_close1 = get_door_ref_colors(1, door1MidX, door1MidY, box1X, box1Y)
col_open2, col_close2 = get_door_ref_colors(2, door2MidX, door2MidY, box2X, box2Y)
col_open3, col_close3 = get_door_ref_colors(3, door3MidX, door3MidY, box3X, box3Y)
 
# allow the camera to warmup
time.sleep(0.1)

if not testMode:
	# Camera Consistency: https://picamera.readthedocs.io/en/release-1.13/recipes1.html
	camera.iso = 100
	# Wait for the automatic gain control to settle
	time.sleep(2)
	# Now fix the values
	#~ camera.shutter_speed = camera.exposure_speed
	camera.shutter_speed = 2 * 33318
	#~ print "speed: {}".format(camera.shutter_speed)
	camera.exposure_mode = 'off'
	#~ g = camera.awb_gains
	#~ print "gains: {}".format(g)
	#~ camera.awb_mode = 'off'
	#~ camera.awb_gains = g

	camera.awb_mode = 'off'
	camera.awb_gains = (Fraction(145, 128), Fraction(679, 256))
	camera.awb_gains = (1.13, 2.65)
	
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
	
	#~ g = camera.awb_gains
	#~ print "gains: {}".format(g)
	
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
	#~ print "Checking Door 1"
	door1open = check_door_open(1, image)
	#~ print "Checking Door 2"
	door2open = check_door_open(2, image)
	#~ print "Checking Door 3"
	door3open = check_door_open(3, image)
	
	# DO DRAWING HERE
	#~ cv2.rectangle(image, (50, 50), (100, 100), (0, 255, 0), 1)
	
	cv2.putText(image, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),(10,500), font, 1,(255,255,255),2,cv2.CV_AA)
	cv2.putText(image, door1open and "door 1 open" or "door 1 closed",(10,500 + 50), font, 1,door1open and (0,255,0) or (0, 0, 255) ,2,cv2.CV_AA)
	cv2.putText(image, door2open and "door 2 open" or "door 2 closed",(10,500 + 100), font, 1,door2open and (0,255,0) or (0, 0, 255) ,2,cv2.CV_AA)
	cv2.putText(image, door3open and "door 3 open" or "door 3 closed",(10,500 + 150), font, 1,door3open and (0,255,0) or (0, 0, 255) ,2,cv2.CV_AA)
 
	# show the frame
	cv2.imshow("Frame", image)
	cv2.setMouseCallback("Frame",draw_circle)
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
