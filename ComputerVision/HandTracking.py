import cv2 as cv
import time
import mediapipe as mp

## Capture Video from Camera
# capture = cv.VideoCapture(1)


#Example Video
video = cv.VideoCapture('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/ComputerVision/Videos/Video3.mp4')


mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


pTime = 0
ctime = 0

while True:
    success, img = video.read()
    # img = img[500:1500, 500:1000, :]
    img = img[500:1300, 350:1700, :]
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv.circle(img, (cx, cy), 15, (255,0,255), cv.FILLED)
              
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (10,10), cv.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    cv.imshow('Video', img)
    cv.waitKey(10)




