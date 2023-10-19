import cv2
import numpy as np
from datetime import datetime


widthImg = 480
heightImg = 640

class Scanner():
    def __init__(self):
        cv2.namedWindow("Trackbars")
        cv2.resizeWindow("Trackbars", 360, 120)
        cv2.createTrackbar("Threshold1", "Trackbars", 10,255, self.nothing)
        cv2.createTrackbar("Threshold2", "Trackbars", 50, 255, self.nothing)

    # finds the edges of the image
    def getContours(self, img):
        biggest = np.array([])
        maxArea = 0
        contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area>5000:
                peri = cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
                if area>maxArea and len(approx) == 4:
                    biggest = approx
                    maxArea = area
        return biggest

    # the image is preprocessed by applying different filters, to find the edges and the text
    def preProcessing(self, img):
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # turning into gray scale image
        imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1) # adding gausian blur
        thres = self.valTrackbars() # getting track bar values
        imgCanny = cv2.Canny(imgBlur, thres[0], thres[1]) # canny blur
        kernel = np.ones((5,5))
        imgDial = cv2.dilate(imgCanny, kernel, iterations=1) # applying dilation
        imgErode = cv2.erode(imgDial, kernel, iterations=1) # applying erosion
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
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
        imgOutput = imgOutput[5:img.shape[0]-5, 5:img.shape[1]-5]
        imgOutput = cv2.resize(imgOutput, (480, 640))
        return imgOutput

    def nothing(x):
        pass
    
        
    # adjust the threshold values to get the desired scan
    def valTrackbars(self):
        Threshold1 = cv2.getTrackbarPos("Threshold1", "Trackbars")
        Threshold2 = cv2.getTrackbarPos("Threshold2", "Trackbars")
        src = Threshold1,Threshold2
        return src
    
    