import cv2 as cv
import time
import mediapipe as mp


capture = cv.VideoCapture(1)

while True:
    success, img = capture.read()

    cv.imshow('Hand', img)
    cv.waitKey(0)




