
# Python program to illustrate HoughLine 
# method for line detection 
import cv2 
import numpy as np 

#img = cv2.imread('shapes/vertical.png') 
#img = cv2.imread('shapes/horizontal.png') 
img = cv2.imread('shapes/horizontal1.png') 
#img = cv2.imread('shapes/l.png') 
  
# Convert the img to grayscale 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
  
# Apply edge detection method on the image 
edges = cv2.Canny(gray,50,150,apertureSize = 3) 

  
# This returns an array of r and theta values 
#lines = cv2.HoughLines(edges,1,np.pi/180, 200) 
minLineLength = 30
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,15,minLineLength,maxLineGap)


print len(lines)
cv2.imshow('test',edges)

  
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

print 'Vertical: ', vertCnt 
print 'Horizontal: ', horCnt
 
# All the changes made in the input image are finally 
# written on a new image houghlines.jpg 
cv2.imshow('lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
