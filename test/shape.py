import numpy as np
import cv2

#img = cv2.imread('shape.png')
#img = cv2.imread('shapes/tri.png')
#img = cv2.imread('shapes/circle.png')
img = cv2.imread('shapes/pent.png')
#img = cv2.imread('shapes/rect0.png')
img = cv2.imread('shapes/sh3.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,57,355,1)
cv2.imshow('thresh',thresh)

_,contours,h = cv2.findContours(thresh,1,2)

contours = sorted(contours, key = cv2.contourArea, reverse = True)[:2]

for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    #print len(approx)
    if len(approx)==5:
        print "pentagon"
        cv2.drawContours(img,[cnt],0,255,-1)
    elif len(approx)==3:
        print "triangle"
        cv2.drawContours(img,[cnt],0,(0,255,0),-1)
    elif len(approx)==4:
        print "square"
        cv2.drawContours(img,[cnt],0,(0,0,255),-1)
    elif len(approx) == 9:
        print "half-circle"
        cv2.drawContours(img,[cnt],0,(255,255,0),-1)
    elif len(approx) > 15:
        print "circle"
        cv2.drawContours(img,[cnt],0,(0,255,255),-1)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
