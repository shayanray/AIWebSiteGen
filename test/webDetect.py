import cv2
import imutils

bInd = 15

#img = cv2.imread('1.jpg')
img = cv2.imread('2.jpg')

img = imutils.resize(img, width=1400)
origImg = img.copy()

imgW, imgH = img.shape[0], img.shape[1]

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgray = cv2.GaussianBlur(imgray,(9,9),0)
#imgray = cv2.medianBlur(imgray,3)

#ret,thresh = cv2.threshold(imgray,127,255,0)
#thresh = cv2.Canny(img,100,200)
thresh = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

contours = sorted(contours, key = cv2.contourArea, reverse = True)[:8]

for cnt in contours:
	area = cv2.contourArea(cnt)
	
	if area < 100:
		continue

	x,y,w,h = cv2.boundingRect(cnt)

	areaDiff = abs(imgW*imgH - (w-x)*(h-y))	
	
	if areaDiff > 0.01:
		cv2.rectangle(img,(x-bInd,y-bInd),(x+w+bInd,y+h+bInd),(0,255,0),2)
	cv2.imshow('test',origImg[y-bInd:y+h+bInd, x-bInd:x+w+bInd])
	cv2.imwrite('0.png',origImg[y-bInd:y+h+bInd, x-bInd:x+w+bInd])
	cv2.waitKey(0)
'''	
drawnCnt = origImg.copy()
cv2.drawContours(drawnCnt, contours, -1, (0,255,0), 3)
cv2.imshow('cnt',drawnCnt)
'''
cv2.imshow('s',thresh)
cv2.imshow('test',img)
cv2.waitKey(0)

