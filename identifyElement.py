import cv2
import numpy as np

minSize = 500

def isCircle(img):
	#cv2.imshow('s',img)
	#cv2.waitKey(0)
	try:
		circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
	except:
		return False
	if len(circles) > 0:
		return True
	circles = np.uint16(np.around(circles))
	return False

def countLines(edges, img):
	minLineLength = 30
	maxLineGap = 10
	lines = cv2.HoughLinesP(edges,1,np.pi/180,15,minLineLength,maxLineGap)
	
	if len(lines) < 100:
		return None

	# The below for loop runs till r and theta values  
	# are in the range of the 2d array 
	vertCnt = 0
	horCnt = 0

	for x in range(0, len(lines)):
	    for x1,y1,x2,y2 in lines[x]:

		if abs(x2-x1) < abs(y2-y1):
			# This is vertical
			vertCnt+=1
			#print 'Vertical'
		else:
			horCnt+=1
			#print 'Horizontal'

		cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
	
	#print 'vert: ', vertCnt
	#print 'horCnt: ', horCnt
	#cv2.imshow('test',img)
	#cv2.waitKey(0)
	if vertCnt > horCnt:
		return 'vertical'
	return 'horizontal'


def getElement(img):
	imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	# Apply edge detection method on the image 
	edges = cv2.Canny(imgray,50,150,apertureSize = 3)
	
	linePos =  countLines(edges,img)

	if linePos is not None:
		if linePos == 'horizontal':
			return 'Main text content'
		elif linePos == 'vertical':
			return 'Navigation Bar'

	#thresh = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
	thresh = edges
	im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	contours = sorted(contours, key = cv2.contourArea, reverse = True)[:3]

	for cnt in contours:
		area = cv2.contourArea(cnt)

		if area < minSize:
			continue

		(x,y,w,h) = cv2.boundingRect(cnt)
		
		# We shouldn't need this code, this is a cheap hack
		'''
		cv2.imwrite('0.png',img)
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
		print abs(w-x)
		print abs(h-y)
		cv2.imshow('sdf', img)
		cv2.waitKey(0)
		exit()
		if abs(w-x) > 3*abs(h-y):
			return 'Navigation Bar'
		'''


		aspectRatio = w / float(h)

		extent = area/float(w*h)

		hull = cv2.convexHull(cnt)
		hullArea = cv2.contourArea(hull)
		solidity = area/float(hullArea)

		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
		'''	
		print 'area: ', area
		print 'aspect ratio: ', aspectRatio
		print 'extent: ', extent
		print 'solidity: ', solidity
		'''
		
		if isCircle(img):
			return 'circle'
		
		if solidity < 0.05 and extent < 0.1:
			return 'I'
		elif solidity < 0.2:
			return 'triangle'
		elif solidity < 0.6:
			return 'X'
		elif solidity < 1.2:
			return 'triangle'
		else:
			return 'Unknown'
		'''
		hullDr = []
		for i in range(len(contours)):
		    # creating convex hull object for each contour
		    hullDr.append(cv2.convexHull(cnt[i], False))

		cv2.drawContours(img, cnt, -1,(0,0,255),-1)
		cv2.drawContours(img, hullDr, -1,(255,0,0),-1)
		'''

	return 'Undefined'
