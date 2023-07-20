
import cv2 as cv
import time
import mediapipe as mp



# pTime = 0
# ctime = 0
    
# video = cv.VideoCapture('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/ComputerVision/Videos/Video1.mp4')
# detector = handModule.handDetector()
# while True:
#         #Example Video
        
#         success, img = video.read()
        
#         # img = img[500:1500, 500:1000, :]
#         img = detector.findHands(img)
#         lmList = detector.findPosition(img)
#         if(len(lmList) != 0):
#             print(lmList[4])

#         cTime = time.time()
#         fps = 1/(cTime-pTime)
#         pTime = cTime
#         cv.putText(img, str(int(fps)), (10,10), cv.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

#         cv.imshow('Video', img)
#         cv.waitKey(1)


