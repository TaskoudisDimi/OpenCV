import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/TutorialOpenCV/Resources/Photos/cat.jpg')
cv.imshow('Cat', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# Simple Thresholding
# 150 is the threshold value. It represents a pixel intensity value. In this command, you are applying a threshold of 150.
# 255 is the maximum pixel value that will be assigned to pixels that meet the threshold condition. 
# In this case, pixels with an intensity greater than or equal to the threshold value (150) will be set to 255 (white).
# cv.THRESH_BINARY is the thresholding type. This specifies the type of thresholding to be applied. 
# In this case, cv.THRESH_BINARY is used, which is a simple binary threshold. 
# Pixels in the image with intensity values greater than or equal to the threshold will be set to the maximum value (255), 
# and pixels with values less than the threshold will be set to the minimum value (0).
# threshold: This variable will store the threshold value itself, which is the value used to distinguish between foreground and 
# background in the image. In this case, it will contain the value 150.
# thresh: This variable will store the result of the thresholding operation. 
# It will be a binary image where pixels exceeding the threshold (150) will be set to 255, and pixels below the threshold will be set to 0, 
# effectively binarizing the image.
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threhold', thresh)


# cv.THRESH_BINARY_INV is a thresholding type in OpenCV used to perform binary thresholding with inversion. 
# When you apply this type of thresholding to an image, it converts it into a binary image where pixel values exceeding 
# the specified threshold are set to one value, typically 0 (black), and pixel values below the threshold are set to another value, 
# typically 255 (white). However, cv.THRESH_BINARY_INV inverts this behavior, which means that:
# Pixels with intensity values greater than or equal to the threshold are set to 0 (black).
# Pixels with intensity values less than the threshold are set to 255 (white).
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threhold Inverse', thresh_inv)

# Adaptive Thresholding
# 255 is the maximum pixel value that will be assigned to pixels that meet the threshold condition. 
# cv.ADAPTIVE_THRESH_MEAN_C is the adaptive method used for thresholding. It indicates that you are using the mean of the neighborhood area to 
# compute the threshold for each pixel. Alternatively, you can use cv.ADAPTIVE_THRESH_GAUSSIAN_C 
# to use the weighted sum of the neighborhood values.
# 11 is the size of the neighborhood or "block size." It defines the size of the region around each pixel that is used to compute 
# the adaptive threshold. In this case, it's an 11x11 neighborhood.
# 3 is a constant subtracted from the mean or weighted sum of the neighborhood values. This value helps fine-tune the threshold.
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)


cv.waitKey()

