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
        # Utilizes the pose instance to process the RGB image.
        self.results = self.pose.process(self.imgRGB)    
        # If pose landmarks are detected in the image, it draws the landmarks on the original image using mpDraw.draw_landmarks.
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
            
        return img 
    
    # Takes an image (img) as input and processes it to find the positions of landmarks.
    def findPosition(self, img, draw=True):
        lmList = []
        if self.results.pose_landmarks:
            # Iterates through the detected landmarks.
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                # Retrieves the (x, y) coordinates of each landmark, scales them according to the image size, and appends them along with the landmark ID to lmList.
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv.circle(img, (cx, cy), 5, (255,0,0), cv.FILLED)
        return lmList
    
