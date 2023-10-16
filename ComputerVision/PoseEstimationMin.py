import cv2 as cv
import mediapipe as mp 
import time

#VIDEO: Advanced Computer Vision with Python 

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

# video = cv.VideoCapture('C:/Users/ASUS/Desktop/Programming/OpenCV/OpenCV/ComputerVision/Videos/Video1.mp4')
video = cv.VideoCapture('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/ComputerVision/Videos/Video1.mp4')


pTime = 0


while True:
    success,img = video.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    print(imgRGB.shape)
    croped = img[500:1500, 500:1000, :]
    results = pose.process(croped)    
    if results.pose_landmarks:
        mpDraw.draw_landmarks(croped, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = croped.shape
            print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv.circle(croped, (cx, cy), 5, (255,0,0), cv.FILLED)


    cTime = time.time()
    fps = 5 /(cTime-pTime)
    pTime = cTime
    cv.putText(croped, str(int(fps)), (70,50), cv.FONT_HERSHEY_PLAIN, 3, (255, 0 , 0), 3)

    cv.imshow('Video', croped)
    cv.waitKey(1)



