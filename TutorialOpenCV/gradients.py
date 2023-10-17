import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/TutorialOpenCV/Resources/Photos/cat.jpg')

cv.imshow('Cat', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
# The Laplacian operator is used for edge detection, highlighting regions of rapid intensity change in the image.
# cv.CV_64F specifies the data type of the output image. It represents a 64-bit floating-point data type.
# np.uint8(np.absolute(lap)) is used to convert the floating-point image (lap) to an 8-bit unsigned integer image, 
# which is typically used for displaying images. The np.absolute() function ensures that all values are positive.
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel
# The Sobel operator is used for edge detection and calculates the gradient in the horizontal and vertical directions.
# cv.CV_64F specifies the data type of the output images. It represents a 64-bit floating-point data type.
# The first Sobel call (sobelx) calculates the gradient in the horizontal direction (1, 0) and represents the horizontal edges.
# The second Sobel call (sobely) calculates the gradient in the vertical direction (0, 1) and represents the vertical edges.
# cv.bitwise_or(sobelx, sobely) combines the horizontal and vertical edge detection results using a bitwise OR operation. 
# This combines the information from both directions and gives you a more complete edge detection result.
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel x', sobely)
cv.imshow('Sobel y', sobely)
cv.imshow('Combined sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)



cv.waitKey(0)