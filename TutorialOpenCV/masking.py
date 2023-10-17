import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/TutorialOpenCV/Resources/Photos/cat.jpg')

cv.imshow('Cat', img)


blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank Image', blank)

# The center of the circle is specified as (image.shape[1]//2, image.shape[0]//2), which calculates the center based on the width and height of the image.
# 100 is the radius of the circle.
# 255 specifies the color of the circle (white).
# -1 indicates that the circle should be filled.
circle = cv.circle(blank, (img.shape[1]//2 + 45,img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', circle)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
cv.imshow('Rectangle', rectangle)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird Shape', weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('masked', masked)


cv.waitKey(0)


