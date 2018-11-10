import cv2
import imutils
import identifyElement as ie

bInd = 15


cntList = []

def insideExistingBox(cnt):
	x,y,w,h = cv2.boundingRect(cnt)
	for cntCmp in cntList:
		#xCmp,yCmp,wCmp,hCmp = cv2.boundingRect(cntCmp)
		xCmp,yCmp,wCmp,hCmp = cntCmp
		if x > xCmp and y > yCmp and x+w < xCmp+wCmp and y+h < yCmp+hCmp:
			return True

	return False

def main():
	#imgPath = 'web0.jpg'	
	imgPath = 'web1.jpg'	

	#img = cv2.imread('1.jpg')
	#img = cv2.imread('2.jpg')
	#origImg = cv2.imread('test/web0.jpg')
	img = cv2.imread(imgPath,0)
	img = imutils.resize(img, width=1400)
	resImg = cv2.imread(imgPath)
	resImg = imutils.resize(resImg, width=1400)
	origImg = img.copy()

	imgH, imgW = img.shape[0], img.shape[1]

	imgray = img
	#imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	imgray = cv2.GaussianBlur(imgray,(9,9),0)
	#imgray = cv2.medianBlur(imgray,3)

	#ret,thresh = cv2.threshold(imgray,127,255,0)
	#thresh = cv2.Canny(img,100,300)
	thresh = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
	im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	contours = sorted(contours, key = cv2.contourArea, reverse = True)[:20]

	elementList = []
	for cnt in contours:
		area = cv2.contourArea(cnt)
		x,y,w,h = cv2.boundingRect(cnt)
		if area < 100 or (imgH == h and imgW == w):
			continue

		if insideExistingBox(cnt):
			continue

		cntList.append((x,y,w,h))


		areaDiff = abs(imgW*imgH - (w-x)*(h-y))	
		
		if areaDiff > 0.01:
			cv2.rectangle(resImg,(x-bInd,y-bInd),(x+w+bInd,y+h+bInd),(0,255,0),2)
		element = ie.getElement(origImg[y-bInd:y+h+bInd, x-bInd:x+w+bInd])
		print element

		pos = None	
		if h < imgH/4 and y < imgH/4:
			# Located at the top
			pos = 'top'
		elif h > imgH - (imgH/5) and y > imgH - (imgH/5):
			# Located at the bottom
			pos = 'bottom'

		elif x > imgW-(imgW/5):
			pos = 'right'
		elif w < imgW/5:
			pos = 'left'
		elif w > imgW/5 and w < imgW-(imgW/5):
			pos = 'center'

		print 'Located on ' + pos
		cv2.imshow('test',origImg[y-bInd:y+h+bInd, x-bInd:x+w+bInd])
		cv2.imwrite('0.png',origImg[y-bInd:y+h+bInd, x-bInd:x+w+bInd])
		cv2.waitKey(0)

		print '\n\n\n\n'
		elementList.append((element, pos))

	print elementList

	cv2.imshow('s',thresh)
	cv2.imshow('test',resImg)
	cv2.waitKey(0)
	return elementList

if __name__ == "__main__":
	main()
