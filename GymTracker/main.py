import PoseModule as pm
import cv2 as cv


video = cv.VideoCapture('')

detector = pm.poseDetector()

while True:
    img = cv.read('')
    img = detector.findPose(img)


    





