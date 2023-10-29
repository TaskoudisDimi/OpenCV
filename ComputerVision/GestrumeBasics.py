import numpy as np
import cv2 as cv
import time 
import HandTrackingModule as track
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume




devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
# volume.SetMasterVolumeLevel(-20.0, None)
minVol = volRange[0]
maxVol = volRange[1]


# video = cv.VideoCapture('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/ComputerVision/Videos/Gym.mp4')

video = cv.VideoCapture(0)

pTime = 0

detector = track.handDetector()
vol = 0
volBar = 400
volPer = 0

while True:
    succces, img = video.read()
    # img = img[150:1500, 150:1500, :]

    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) //2, (y1 + y2) //2

        cv.circle(img, (x1, y1), 5, (255, 0, 255), cv.FILLED)
        cv.circle(img, (x2, y2), 5, (255, 0, 255), cv.FILLED)
        cv.line(img, (x1,y1), (x2,y2), (255,0,255), 3)
        cv.circle(img, (cx, cy), 5, (255, 0, 255), cv.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)
        # print(length)
       

        vol = np.interp(length, [50, 300], [minVol, maxVol])
        volBar = np.interp(length, [50, 300], [400, 150])
        volPer = np.interp(length, [50, 300], [0,100])
        # print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
            cv.circle(img, (cx, cy), 5, (0,255,0), cv.FILLED)


    cv.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
    cv.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv.FILLED)
    cv.putText(img, f'{int(volPer)} %', (40, 450), cv.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 3)


    cv.imshow('Video', img)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img, f'FPS {int(fps)}', (20, 70), cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    cv.imshow("Video", img)

    # Break the loop when the user presses the 'q' key
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


video.release()
cv.destroyAllWindows()








