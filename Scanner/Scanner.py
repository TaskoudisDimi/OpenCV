import cv2 as cv
import time


frameWidth = 640
frameHeight = 480

cap = cv.VideoCapture('')
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 130)
while True:
    success, img = cap.read()
    cv.imshow("Result", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
