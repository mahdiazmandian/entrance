import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import math

#searchBoxX = 10
#searchBoxY = 3
img = np.zeros((1,1,3), np.uint8)

dummy_img = np.zeros((1,1,3), np.uint8)

door1MidX = 175
door1MidY = 451
box1X = 5
box1Y = 10

door2MidX = 964
door2MidY = 576
box2X = 5
box2Y = 10

door3MidX = 1381
door3MidY = 597
box3X = 5
box3Y = 10


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


#~ def check_door_open(door_num)
        
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),100,(255,0,0),-1)
        print 'clicked: ({}, {})'.format(x, y)


#~ # Create a black image
#~ img = np.zeros((512,512,3), np.uint8)
#~ # Draw a diagonal blue line with thickness of 5 px
#~ cv.line(img,(0,0),(511,511),(255,0,0),5)

#~ cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

#~ cv.circle(img,(447,63), 63, (0,0,255), -1)

#~ cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

#~ pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#~ pts = pts.reshape((-1,1,2))
#~ cv.polylines(img,[pts],True,(0,255,255))

#~ font = cv.FONT_HERSHEY_SIMPLEX
#~ #cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

#~ #cv.imwrite('drawing.png',img)
#~ cv.imshow('image',img)
#~ cv.waitKey(0)
#~ cv.destroyAllWindows()

#~ img = cv.imread('door_open.jpg',0)
#~ img = cv.imread('door_closed.jpg')


def getAverageColorOfBox(fileName, img, x, y, searchBoxX, searchBoxY):
        if not fileName == '':
                img = cv.imread(fileName)
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
        
        print "Mid Color: ({}, {}, {})".format(img[y, x, 0], img[y, x, 1], img[y, x, 2])
        
        #~ print sumR, sumG, sumB
        
        cv.rectangle(img, (x - searchBoxX, y - searchBoxY), (x + searchBoxX, y + searchBoxY), (0, 255, 0), 1)


        cv.namedWindow('image')
        cv.setMouseCallback('image',draw_circle)
        cv.imshow('image',img)
        cv.waitKey(0)
        cv.destroyAllWindows()
        return sumR, sumG, sumB

def getColorDist(r0, g0, b0, r1, g1, b1):
        return math.sqrt((r0 - r1)**2 + (g0 - g1)**2 + (b0 - b1)**2)


# Initialization
col_open1, col_close1 = get_door_ref_colors(1, door1MidX, door1MidY, box1X, box1Y)
#~ col_open2, col_close2 = get_door_ref_colors(2, door2MidX, door2MidY, box2X, box2Y)
#~ col_open3, col_close3 = get_door_ref_colors(3, door3MidX, door3MidY, box3X, box3Y)

#~ img = cv.imread('door_open.jpg')
#~ x = 303
#~ y = 52
#~ radius = 0
#~ thickness = 1
#~ cv.circle(img, (x, y), radius, (0, 255, 0), 1)testR, testG, testB = getAverageColorOfBox('test_open.jpg', 303, 52)





