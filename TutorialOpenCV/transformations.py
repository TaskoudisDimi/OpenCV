import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/TutorialOpenCV/Resources/Photos/park.jpg')

# Translation
def translate(image, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (image.shape[1], image.shape[0])
    # warpAffine() function is the size of the output image, which should be in the form of **(width, height)**. Remember width = number of columns, and height = number of rows.
    return cv.warpAffine(image, transMat, dimensions)

# -x --> Left
# -y --> Up
# -x --> Right
# -y --> Down

translated = translate(img, -100, 100)

def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]
    if(rotPoint is None):
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Boston', rotated)


# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)


# Flipping
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)


cv.waitKey(0)

