
import cv2 as cv
import time
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector


cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)


while True:
    success, img = cap.read()
    img = cv.cvtColor( img, cv.COLOR_BGR2RGB)
    img = detector.findHands(img)
    # lmlist, _ = detector.findPosition(img)
    cv.imshow("Image", img)
    cv.waitKey(1)




