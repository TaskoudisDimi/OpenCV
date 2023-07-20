
import cv2 as cv
import time
import mediapipe as mp
from HandTrackingModule import handDetector


pTime = 0
ctime = 0
    
video = cv.VideoCapture('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/ComputerVision/Videos/Video1.mp4')
detector = handDetector()

while True:
        
        success, img = video.read()

        img = detector.findHands(img)
        lmList = detector.findPosition(img)        
        
        cv.imshow('Video', img)
        cv.waitKey(1)


