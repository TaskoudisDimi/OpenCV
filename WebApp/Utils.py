
import numpy as np
import cv2 as cv
import mediapipe as mp 
import time
import math
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



def Segmentation_Image(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, threshold = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    kernel = np.ones([3,3], np.uint8)
    opening = cv.morphologyEx(threshold, cv.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv.dilate(opening, kernel, iterations=3)
    dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
    ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)
    sure_fg = np.uint8(sure_fg)
    unknown = cv.subtract(sure_bg,sure_fg)
    ret, markers = cv.connectedComponents(sure_fg)
    markers = markers+1
    markers[unknown==255] = 0
    markers = cv.watershed(img,markers)
    img[markers == -1] = [0,0,255]
    return img



def From_Image_to_Text():
    pass



widthImg = 480
heightImg = 640

class UtilScanner():
    def __init__(self):
        pass
        # cv.namedWindow("Trackbars")
        # cv.resizeWindow("Trackbars", 360, 120)
        # cv.createTrackbar("Threshold1", "Trackbars", 10,255, self.nothing)
        # cv.createTrackbar("Threshold2", "Trackbars", 50, 255, self.nothing)

    # finds the edges of the image
    def getContours(self, img):
        biggest = np.array([])
        maxArea = 0
        contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        for cnt in contours:
            area = cv.contourArea(cnt)
            if area>5000:
                peri = cv.arcLength(cnt, True)
                approx = cv.approxPolyDP(cnt, 0.02*peri, True)
                if area>maxArea and len(approx) == 4:
                    biggest = approx
                    maxArea = area
        return biggest

    # the image is preprocessed by applying different filters, to find the edges and the text
    def preProcessing(self, img):
        imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # turning into gray scale image
        imgBlur = cv.GaussianBlur(imgGray, (5,5), 1) # adding gausian blur

        imgCanny = cv.Canny(imgBlur, 10, 50) # canny blur
        kernel = np.ones((5,5))
        imgDial = cv.dilate(imgCanny, kernel, iterations=1) # applying dilation
        imgErode = cv.erode(imgDial, kernel, iterations=1) # applying erosion
        return imgErode

    # calculates the four courner points of the image
    def reorder(self, myPoints):
        myPoints = myPoints.reshape((4,2))
        myPointsNew = np.zeros((4, 1, 2), np.int32)
        add = myPoints.sum(1)
        myPointsNew[0] = myPoints[np.argmin(add)]
        myPointsNew[3] = myPoints[np.argmax(add)]
        diff = np.diff(myPoints, axis=1)
        myPointsNew[1] = myPoints[np.argmin(diff)]
        myPointsNew[2] = myPoints[np.argmax(diff)]
        return myPointsNew

    # the image is cropped at the edges, with the obtained four points(co-ordinates)
    def getWarp(self, img, biggest):
        biggest = self.reorder(biggest)
        pts1 = np.float32(biggest)
        pts2 = np.float32([[0,0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
        matrix = cv.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv.warpPerspective(img, matrix, (widthImg, heightImg))
        imgOutput = imgOutput[5:img.shape[0]-5, 5:img.shape[1]-5]
        imgOutput = cv.resize(imgOutput, (480, 640))
        return imgOutput

    def nothing(x):
        pass


    

# class poseDetector():
#     def __init__(self, mode=False, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5):
#         self.mode = mode
#         self.upBody = upBody
#         self.smooth = smooth
#         self.detectionCon = detectionCon
#         self.trackCon = trackCon
#         self.mpDraw = mp.solutions.drawing_utils
#         self.mpPose = mp.solutions.pose
#         # self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth, self.detectionCon, self.trackCon)
#         self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth)

#     def findPose(self, img, draw=True):

#         self.imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#         # Utilizes the pose instance to process the RGB image.
#         self.results = self.pose.process(self.imgRGB)    
#         # If pose landmarks are detected in the image, it draws the landmarks on the original image using mpDraw.draw_landmarks.
#         if self.results.pose_landmarks:
#             if draw:
#                 self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
            
#         return img 
    
#     # Takes an image (img) as input and processes it to find the positions of landmarks.
#     def findPosition(self, img, draw=True):
#         lmList = []
#         if self.results.pose_landmarks:
#             # Iterates through the detected landmarks.
#             for id, lm in enumerate(self.results.pose_landmarks.landmark):
#                 # Retrieves the (x, y) coordinates of each landmark, scales them according to the image size, and appends them along with the landmark ID to lmList.
#                 h, w, c = img.shape
#                 # print(id, lm)
#                 cx, cy = int(lm.x * w), int(lm.y * h)
#                 lmList.append([id, cx, cy])
#                 if draw:
#                     cv.circle(img, (cx, cy), 5, (255,0,0), cv.FILLED)
#         return lmList


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=False, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

    def findHands(self, img, draw=True):    # Finds all hands in a frame
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self, img, handNo=0, draw=True):   # Fetches the position of hands
        xList = []
        yList = []
        bbox = []
        self.lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                xList.append(cx)
                yList.append(cy)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv.circle(img, (cx, cy), 5, (255, 0, 255), cv.FILLED)

            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            bbox = xmin, ymin, xmax, ymax

            if draw:
                cv.rectangle(img, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20),
                              (0, 255, 0), 2)

        return self.lmList, bbox

    def fingersUp(self):    # Checks which fingers are up
        fingers = []
        # Thumb
        if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Fingers
        for id in range(1, 5):

            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # totalFingers = fingers.count(1)

        return fingers

    def findDistance(self, p1, p2, img, draw=True,r=15, t=3):   # Finds distance between two fingers
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        if draw:
            cv.line(img, (x1, y1), (x2, y2), (255, 0, 255), t)
            cv.circle(img, (x1, y1), r, (255, 0, 255), cv.FILLED)
            cv.circle(img, (x2, y2), r, (255, 0, 255), cv.FILLED)
            cv.circle(img, (cx, cy), r, (0, 0, 255), cv.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)

        return length, img, [x1, y1, x2, y2, cx, cy]






