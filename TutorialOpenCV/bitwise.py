import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/TutorialOpenCV/Resources/Photos/cat.jpg')

cv.imshow('Cat', img)



blank = np.zeros((400,400), dtype='uint8')

# (30, 30) and (370, 370) are the coordinates of the top-left and bottom-right corners of the rectangle
# 255 is the color of the rectangle. 
# -1 is the thickness parameter. When the thickness is set to a negative value (such as -1), 
# it indicates that you want to draw a filled rectangle. In this case, the entire area within the specified coordinates will be filled with the color specified (white in this case).
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)


# bitwise AND --> intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise And', bitwise_and)


# bitwise OR --> non-intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)


# bitwise XOR --> non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# bitwise NOT
bitwise_not = cv.bitwise_not(rectangle, circle)
cv.imshow('Bitwise NOT', bitwise_not)

cv.waitKey(0)
