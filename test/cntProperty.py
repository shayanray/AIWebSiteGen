import cv2

minSize = 500

#img = cv2.imread('shapes/i1.png')         
#img = cv2.imread('shapes/hourglass1.png')         
img = cv2.imread('shapes/tri1.png')         
img = cv2.imread('shapes/x1.png')         

# Convert the img to grayscale 
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Apply edge detection method on the image 
edges = cv2.Canny(imgray,50,150,apertureSize = 3)
#thresh = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
thresh = edges
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print len(contours)
contours = sorted(contours, key = cv2.contourArea, reverse = True)[:1]

for cnt in contours:
	area = cv2.contourArea(cnt)

	if area < minSize:
		continue

	print '----------------'
	(x,y,w,h) = cv2.boundingRect(cnt)

	aspectRatio = w / float(h)

	extent = area/float(w*h)

	hull = cv2.convexHull(cnt)
	hullArea = cv2.contourArea(hull)
	solidity = area/float(hullArea)

	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

	print 'area: ', area
	print 'aspect ratio: ', aspectRatio
	print 'extent: ', extent
	print 'solidity: ', solidity

	hullDr = []
	for i in range(len(contours)):
	    # creating convex hull object for each contour
	    hullDr.append(cv2.convexHull(cnt[i], False))

	cv2.drawContours(img, cnt, -1,(0,0,255),-1)
	cv2.drawContours(img, hullDr, -1,(255,0,0),-1)

	cv2.imshow('test',img)
	cv2.waitKey(0)

cv2.imshow('test',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

