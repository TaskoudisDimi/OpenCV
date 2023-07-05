import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

# RGB colors
# plt.imshow(img)
# plt.show()



# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(img, cv.COLOR_HSV2BGR)
cv.imshow('HSV_BGR', hsv_bgr)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)
