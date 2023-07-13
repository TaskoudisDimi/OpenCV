import cv2 as cv
import numpy as np
import time
import PoseModule as pm


video = cv.VideoCapture('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/ComputerVision/Videos/Video1.mp4')

detector = pm.poseDetector()


while True:
    success, img = video.read()
    img = cv.resize(img, (600, 600))
    img = detector.findPose(img)
    
    cv.imshow("Image", img)
    cv.waitKey(100)

