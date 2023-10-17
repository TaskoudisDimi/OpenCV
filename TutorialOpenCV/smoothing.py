import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/TutorialOpenCV/Resources/Photos/cat.jpg')

cv.imshow('Cat', img)

# Average
# cv.blur() is used to apply average (mean) blurring to the input image. 
# It smoothes the image by replacing each pixel's value with the average value of the pixels in a specified neighborhood.
# (7, 7) specifies the size of the neighborhood (7x7 in this case) used to compute the average for each pixel.
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# cv.GaussianBlur() applies Gaussian blurring to the image. It's a smoothing technique that replaces each pixel's value 
# with a weighted average of the pixels in a neighborhood.
# (7, 7) specifies the size of the Gaussian kernel, which defines the extent of the weighted average. A larger kernel results in more smoothing.
# 0 is the standard deviation of the Gaussian distribution. In this case, it's set to 0, 
# indicating that OpenCV will automatically calculate an appropriate value based on the kernel size.
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

# cv.medianBlur() is used to apply median blurring to the image. It replaces each pixel's value with the median value of the pixels in a neighborhood.
# 7 specifies the size of the neighborhood (7x7 in this case) used for the median calculation.
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

# cv.bilateralFilter() applies bilateral filtering to the image. It is a smoothing technique that preserves edges 
# while smoothing regions of homogeneous color.
# 10 is the diameter of the pixel neighborhood used during filtering.
# 15 and 15 are the filter sigma values, which control the influence of the pixel intensity differences and spatial differences, respectively.
bilateral = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)



