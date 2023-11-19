
import numpy as np
import cv2 as cv
import mediapipe as mp 
import time
# from openpyxl import Workbook


def FromBGR_To_Gray(img):
    # Convert the image to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return gray


def FromGray_To_Lap(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    lap = cv.Laplacian(gray, cv.CV_64F)
    lap = np.uint8(np.absolute(lap))
    return lap


def FromGray_To_Canny(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    canny = cv.Canny(gray, 150, 175)
    return canny



def FromImage_To_Blue(img):
    # blank is initialized as a blank (black) image. It is created using NumPy with the same dimensions as the first two dimensions of the img shape. 
    blank = np.zeros(img.shape[:2], dtype='uint8')
    b,g,r = cv.split(img)
    blue = cv.merge([b,blank,blank])
    return blue

def FromImage_To_Green(img):
    # blank is initialized as a blank (black) image. It is created using NumPy with the same dimensions as the first two dimensions of the img shape. 
    blank = np.zeros(img.shape[:2], dtype='uint8')
    b,g,r = cv.split(img)
    green = cv.merge([blank,g,blank])
    return green

def FromImage_To_Red(img):
    # blank is initialized as a blank (black) image. It is created using NumPy with the same dimensions as the first two dimensions of the img shape. 
    blank = np.zeros(img.shape[:2], dtype='uint8')
    b,g,r = cv.split(img)
    red = cv.merge([blank,blank,r])
    return red


def Detect_Faces(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    haar_cascade = cv.CascadeClassifier('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/TutorialOpenCV/haar_face.xml')
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
    print(f'Number of faces found = {len(faces_rect)}')
    for (x,y,w,h) in faces_rect:
        cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
    return img


def Resize_Image(img, width, height):
    img = cv.resize(img, (width, height), cv.INTER_CUBIC)
    return img



def Segmentation_Image():
    pass



def From_Image_to_Text():
    pass



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
    

# detector = estimator.poseDetector()

# while True:
#     success,img = video.read()
#     croped = img[500:1500, 500:1000, :]
#     croped = detector.findPose(croped)
#     lmList = detector.findPosition(croped, draw=False)
#     if len(lmList)!=0:
#         cv.circle(croped, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv.FILLED)
#     cTime = time.time()
#     fps = 5 /(cTime-pTime)
#     pTime = cTime

#     cv.putText(croped, str(int(fps)), (70,50), cv.FONT_HERSHEY_PLAIN, 3, (255, 0 , 0), 3)

#     cv.imshow('Video', croped)
#     cv.waitKey(1)