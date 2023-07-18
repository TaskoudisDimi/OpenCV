import cv2 as cv
import time
import mediapipe as mp

## Capture Video from Camera
# capture = cv.VideoCapture(1)


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):

        self.mode = mode
        self.maxHands = maxHands        
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img):
        img = img[500:1500, 500:1000, :]
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv.circle(img, (cx, cy), 25, (255,0,255), cv.FILLED)
                    
                self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)





def main():
    pTime = 0
    ctime = 0
    
    #Example Video
    video = cv.VideoCapture('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/ComputerVision/Videos/Video1.mp4')

    while True:
        success, img = video.read()
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv.putText(img, str(int(fps)), (10,10), cv.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

        cv.imshow('Video', img)
        cv.waitKey(1)



if __name__ == "__main__":
    main()