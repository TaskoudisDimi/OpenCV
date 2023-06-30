import cv2 as cv

img = cv.imread('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/Resources/Photos/cat.jpg')


# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


cv.imshow('Cat', img)

cv.waitKey(0)
