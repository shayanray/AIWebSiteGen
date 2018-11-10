import numpy as np
import cv2 as cv
#img = cv.imread('shapes/circle.png',0)
img = cv.imread('shapes/circle1.png',0)
#img = cv.imread('shapes/tri1.png',0)
#img = cv.imread('shapes/1.jpg',0)
#img = cv.imread('shapes/i.png')
img = cv.medianBlur(img,5)
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,param1=200,param2=70,minRadius=50,maxRadius=300)
circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,param1=70,param2=50,minRadius=50,maxRadius=300)
if circles is None:
	print 'No circles detected'
	exit()

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
cv.imshow('detected circles',cimg)
cv.waitKey(0)
cv.destroyAllWindows()
