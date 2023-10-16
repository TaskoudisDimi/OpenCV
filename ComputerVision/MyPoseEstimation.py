
import cv2 as cv
import PoseModule as estimator
import time

video = cv.VideoCapture('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/ComputerVision/Videos/Video3.mp4')

pTime = 0

detector = estimator.poseDetector()

while True:
    success,img = video.read()
    croped = img[500:1500, 500:1000, :]
    croped = detector.findPose(croped)
    lmList = detector.findPosition(croped, draw=False)
    if len(lmList)!=0:
        cv.circle(croped, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv.FILLED)
    cTime = time.time()
    fps = 5 /(cTime-pTime)
    pTime = cTime

    cv.putText(croped, str(int(fps)), (70,50), cv.FONT_HERSHEY_PLAIN, 3, (255, 0 , 0), 3)

    cv.imshow('Video', croped)
    cv.waitKey(1)



