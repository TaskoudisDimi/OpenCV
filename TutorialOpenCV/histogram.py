import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/TutorialOpenCV/Resources/Photos/cats.jpg')

cv.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# cv.imshow('Circle', circle)


mask = cv.bitwise_and(img, img, mask=circle)
cv.imshow('Mask', mask)



# #Grayscale histogram
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])
# plt.figure()
# plt.title('GrayScale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()


plt.figure()
plt.title('GrayScale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b','g','r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()


cv.waitKey(0)

