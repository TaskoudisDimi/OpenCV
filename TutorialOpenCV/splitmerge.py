import cv2 as cv
import numpy as np


img = cv.imread('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/TutorialOpenCV/Resources/Photos/cat.jpg')
print(img.shape)
cv.imshow('Cat', img)

# blank is initialized as a blank (black) image. It is created using NumPy with the same dimensions as the first two dimensions of the img shape. 
blank = np.zeros(img.shape[:2], dtype='uint8')
print(blank.shape)

# cv.split(img) is used to split the input image img into its color channels. After this line, b, g, and r 
# will each hold the blue, green, and red color channels of the original image, respectively.
b,g,r = cv.split(img)

# cv.merge() is used to create a new image by merging specified channels. 
# In this case, we are merging the blue channel (b) with two blank channels (filled with zeros) for green and red. 
# As a result, the blue variable will hold an image with only the blue channel from the original image, 
# while the green and red channels will be set to 0 (black).
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])


cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)


cv.waitKey(0)
