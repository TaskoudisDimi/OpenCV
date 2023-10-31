
import numpy as np
import cv2 as cv


def FromBGR_To_Gray(img):
    img = cv.imread(img)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return gray


# gray = FromBGR_To_Gray(img)
# cv.imshow('Gray', gray)



# cv.waitKey(0)
