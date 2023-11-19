import numpy as np
import cv2 as cv


# img = cv.imread('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/TutorialOpenCV/Resources/Photos/coins.jpg')

img = cv.imread('D:/Programming/OpenCV/OpenCV/TutorialOpenCV/Resources/Photos/cat.jpg')



gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Thresholding: Applies thresholding to the grayscale image using Otsu's thresholding method to obtain a binary image. This process separates objects from the background.
ret, threshold = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
# cv.imshow('opening', threshold)

kernel = np.ones([3,3], np.uint8)
#Morphological Operations: Performs morphological opening to remove noise and smoothen the binary image.
opening = cv.morphologyEx(threshold, cv.MORPH_OPEN, kernel, iterations=2)
# cv.imshow('opening', opening)

# Dilates the result of the morphological opening to enhance the foreground objects.
sure_bg = cv.dilate(opening, kernel, iterations=3)
# cv.imshow('sure_bg', sure_bg)

# Calculates the distance of each pixel to the nearest zero pixel (background). This information is used for segmentation.
dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
# cv.imshow('dist_transform', dist_transform)

# Applies another threshold to the distance-transformed image to identify regions that are the 'sure foreground.'
ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# cv.imshow('sure_fg', sure_fg)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
# Using the 'sure background' and 'sure foreground,' the code finds the unknown regions by subtracting 'sure foreground' from 'sure background.'
unknown = cv.subtract(sure_bg,sure_fg)
# cv.imshow('unknown', unknown)


# Marker labelling
# Performs connected component analysis on the 'sure foreground' to label different regions.
ret, markers = cv.connectedComponents(sure_fg)
# Add one to all labels so that sure background is not 0, but 1
# Modifies the markers array for watershed segmentation by marking sure background as 1 and unknown regions as 0.
markers = markers+1
# Now, mark the region of unknown with zero
markers[unknown==255] = 0

# Applies the watershed algorithm to the original image using the modified markers.
markers = cv.watershed(img,markers)
img[markers == -1] = [0,0,255]


cv.imshow('Park', img)
cv.waitKey()
















