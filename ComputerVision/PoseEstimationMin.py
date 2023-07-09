import cv2 as cv
import mediapipe as mp 
import time

video = cv.VideoCapture('C:/Users/ASUS/Desktop/Programming/OpenCV/OpenCV/ComputerVision/Videos/Video1.mp4')

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils


pTime = 0


while True:
    success,img = video.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = pose.process(imgRGB)    

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks)

    cTime = time.time()
    fps = 1 /(cTime-pTime)
    pTime = cTime

    cv.putText(img, str(int(fps)), (70,50), cv.FONT_HERSHEY_PLAIN, 3, (255, 0 , 0), 3)
    cv.imshow('Video', img)
    cv.waitKey(1) 

