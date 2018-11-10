import cv2

img = cv2.imread('0.jpg')

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#imgray = cv2.GaussianBlur(imgray,(5,5),0)
#imgray = cv2.medianBlur(imgray,3)

#ret,thresh = cv2.threshold(imgray,127,255,0)
#thresh = cv2.Canny(img,100,200)
thresh = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow('s',thresh)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

contours = sorted(contours, key = cv2.contourArea, reverse = True)[:5]

for cnt in contours:
	peri = cv2.arcLength(cnt, True)
	approx = cv2.approxPolyDP(cnt, 0.2 * peri, True)
	
	#if len(approx) > 3:
	#print cv2.contourArea(cnt)
	#cv2.drawContours(img, cnt, -1, (0,255,0), 3)
	#cv2.imshow('test',img)
	#cv2.waitKey(0)

	x,y,w,h = cv2.boundingRect(cnt)
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
	
#cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.imshow('test',img)
cv2.waitKey(0)

