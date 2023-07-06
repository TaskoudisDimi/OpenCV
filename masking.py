import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/Resources/Photos/cat.jpg')

cv.imshow('Cat', img)


blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank Image', blank)

circle = cv.circle(blank, (img.shape[1]//2 + 45,img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', circle)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
cv.imshow('Rectangle', rectangle)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird Shape', weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('masked', masked)


cv.waitKey(0)


