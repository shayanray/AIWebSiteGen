import cv2

#img = cv2.imread('1.jpg')
img = cv2.imread('tri.png')

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#imgray = cv2.GaussianBlur(imgray,(5,5),0)
#imgray = cv2.medianBlur(imgray,3)

#ret,thresh = cv2.threshold(imgray,127,255,0)
#thresh = cv2.Canny(img,100,200)
thresh = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow('s',thresh)
#im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

contours = sorted(contours, key = cv2.contourArea, reverse = True)[:2]

	
#cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.drawContours(img, contours, 1, (0,255,0), 3)

cv2.imshow('test',img)
cv2.waitKey(0)

