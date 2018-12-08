import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

searchBoxX = 10
searchBoxY = 3
        
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


def getAverageColorOfBox(fileName, x, y):
        img = cv.imread(fileName)
        sumR = 0
        sumG = 0
        sumB = 0

        for pixelX in range(x - searchBoxX, x + searchBoxX + 1):
                for pixelY in range(y - searchBoxY, y + searchBoxY + 1):
                        sumR += img[y, x, 0]
                        sumG += img[y, x, 1]
                        sumB += img[y, x, 2]
                        #~ print img[y, x, 0], img[y, x, 1], img[y, x, 2]
        factor = (2 * searchBoxX + 1)  * (2 * searchBoxY + 1)
        sumR /= factor
        sumG /= factor
        sumB /= factor
        
        print sumR, sumG, sumB
        
        cv.rectangle(img, (x - searchBoxX, y - searchBoxY), (x + searchBoxX, y + searchBoxY), (0, 255, 0), 1)


        cv.namedWindow('image')
        cv.setMouseCallback('image',draw_circle)
        cv.imshow('image',img)
        cv.waitKey(0)
        cv.destroyAllWindows()


getAverageColorOfBox('door_open.jpg', 303, 52)
getAverageColorOfBox('door_closed.jpg', 303, 52)
#~ img = cv.imread('door_open.jpg')
#~ x = 303
#~ y = 52
#~ radius = 0
#~ thickness = 1
#~ cv.circle(img, (x, y), radius, (0, 255, 0), 1)



