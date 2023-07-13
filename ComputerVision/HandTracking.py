import cv2 as cv
import time
import mediapipe as mp

## Capture Video from Camera
# capture = cv.VideoCapture(1)


#Example Video
video = cv.VideoCapture('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/ComputerVision/Videos/Video1.mp4')


mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


while True:
    success, img = video.read()
    img = img[500:1500, 500:1000, :]
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv.imshow('Video', img)
    cv.waitKey(1)




