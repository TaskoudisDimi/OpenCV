import cv2 as cv
import numpy as np
import imutils
import matplotlib.pyplot as plt


cap = cv.VideoCapture('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/ComputerVision/Videos/tennis2.mp4')


def rescaleFrame(frame, scale = 0.50):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# redLower = np.array([0,10,170], dtype='uint8')
# redUpper = np.array([50,50,255], dtype='uint8')
yellowLower = np.array([20, 100, 100], dtype='uint8')
yellowUpper = np.array([40, 255, 255], dtype='uint8')

c = 0


while True:
    grapped,frame=cap.read()
    frame = rescaleFrame(frame)
    yellow= cv.inRange(frame,yellowLower,yellowUpper)
    yellow = cv.GaussianBlur(yellow,(3,3),0)

    cnts = cv.findContours(yellow.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    print(cnts)
    if len(cnts) > 0:
        cnt = sorted(cnts,key=cv.contourArea,reverse=True)[0]
        rect = np.int32(cv.boxPoints(cv.minAreaRect(cnt)))
        cv.circle(frame, (rect[0][0]+(rect[-1][0] - rect[0][0])//2,rect[1][1]+(rect[-1][-1]-rect[1][1])//2), 25, (0, 255, 0), -1)
    cv.imshow("Ball Tracking", frame)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break
        


# cleanup the camera and close any open windows
cap.release()
cv.destroyAllWindows()
