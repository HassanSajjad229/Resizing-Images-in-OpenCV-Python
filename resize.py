import cv2

a=cv2.imread('a.jpg',1)

scale_percent = 50 # percent of original size
width = int(a.shape[1] * scale_percent / 100)
height = int(a.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv2.resize(a, dim, interpolation = cv2.INTER_AREA)

cv2.imshow('Original',a)  
cv2.imshow('Tested',resized)  
cv2.waitKey(0)
cv2.destroyAllWindows()