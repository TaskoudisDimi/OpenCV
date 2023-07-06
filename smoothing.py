import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/Resources/Photos/cat.jpg')

cv.imshow('Cat', img)

# Average
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)


gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

bilateral = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow('Bilateral', bilateral)



cv.waitKey(0)

