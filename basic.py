import cv2 as cv


img = cv.imread('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/Resources/Photos/cat.jpg')


# # Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Cat', gray)


# # Blur
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# # cv.imshow('Cat', blur)

# # Edge Cascade
# canny = cv.Canny(blur, 125, 175)
# # cv.imshow('Cat', canny)

# # Dilating the image
# dilated = cv.dilate(canny, (7,7), iterations = 3)
# # cv.imshow('Cat', dilated)

# # Eroding
# eroded = cv.erode(dilated, (3,3), iterations = 1)
# # cv.imshow('Cat', eroded)

# # Resize
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Cat', resized)

# # Copping
# cropped = img[50:200, 200:400]
# cv.imshow('Cat', cropped)


cv.waitKey(0)
