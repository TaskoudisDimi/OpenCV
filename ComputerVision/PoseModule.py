import cv2 as cv
import mediapipe as mp 
import time


class poseDetector():
    def __init__(self, mode=False, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5):

        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon


        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        # self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth, self.detectionCon, self.trackCon)
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth)

    def findPose(self, img, draw=True):

        self.imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        # croped = img[500:1500, 500:1000, :]
        self.results = self.pose.process(self.imgRGB)    

        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
            
        return img 
    def findPosition(self, img, draw=True):
        lmList = []
        if self.results.pose_landmarks:

            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv.circle(img, (cx, cy), 5, (255,0,0), cv.FILLED)
        return lmList
    
def main():
     # video = cv.VideoCapture('C:/Users/ASUS/Desktop/Programming/OpenCV/OpenCV/ComputerVision/Videos/Video1.mp4')
    video = cv.VideoCapture('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/ComputerVision/Videos/Video1.mp4')

    pTime = 0

    detector = poseDetector()

    while True:
        success,img = video.read()
        croped = img[500:1500, 500:1000, :]
        croped = detector.findPose(croped)

        cTime = time.time()
        fps = 5 /(cTime-pTime)
        pTime = cTime

        cv.putText(croped, str(int(fps)), (70,50), cv.FONT_HERSHEY_PLAIN, 3, (255, 0 , 0), 3)

        cv.imshow('Video', croped)
        cv.waitKey(1)




main()

