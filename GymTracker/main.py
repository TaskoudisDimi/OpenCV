import PoseModule as pm
import cv2 as cv
from PoseModule import poseDetector
import numpy as np

video = cv.VideoCapture('C:/Users/chris/Desktop/Dimitris/Tutorials/Videos/Video2.mp4')

detector = poseDetector()

count = 0
dir = 0

while True:
    success, img = video.read()
    # img = cv.resize(img, (850,640))
    img = cv.resize(img, (450,640))
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
        angle = detector.findAngle(img, 12, 14, 16)
        per = np.interp(angle, (210, 310), (0, 100))
        bar = np.interp(img, (220, 310), (650, 100))
        # print(angle, per)

        if per == 100:
            if dir == 0:
                count += 0.5
                dir = 1

        if per == 0:
            if dir == 1:
                count += 0.5
                dir = 0
        
        # cv.rectangle(img, (300, 100), (375, 650), (0, 255, 0), 3)
        # cv.rectangle(img, (300, int(bar)), (300, 650), (0, 255, 0), cv.FILLED)
        cv.putText(img, f'{int(per)} %', (300, 75), cv.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 4)
        
        cv.putText(img, str(int(count)), (50, 100), cv.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

    cv.imshow("Video", img)

    # Break the loop when the user presses the 'q' key
    if cv.waitKey(1) & 0xFF == ord('q'):
        break



video.release()

cv.destroyAllWindows()

    





