import cv2
import numpy as np
from datetime import datetime
from ScannerModule import Scanner


# Remove the noise
# Edge Detection
# Contour Extraction
# Best Contour Selection
# Best Contour Selection


widthImg = 480
heightImg = 640

scan = Scanner()

while True:
    img = cv2.imread('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/Scanner/Resources/paper.jpg')
    img = cv2.resize(img, (widthImg, heightImg)) # resizing the image
    cv2.imshow("Original", img)
    imgProcessed = scan.preProcessing(img)

    biggest = scan.getContours(imgProcessed)
    # print(biggest)
    if biggest.size != 0:
        imgWarp = scan.getWarp(img, biggest)
        
        # applying adaptive threshold
        imgWarpGray = cv2.cvtColor(imgWarp,cv2.COLOR_BGR2GRAY)
        imgAdaptiveThre= cv2.adaptiveThreshold(imgWarpGray, 255, 1, 1, 7, 2)
        imgResult = cv2.bitwise_not(imgAdaptiveThre)

    else:
        # blank image
        imgResult = np.zeros((heightImg,widthImg, 3), np.uint8)
        
    # we get the three forms of the scanned document
    cv2.imshow('warp', imgWarp)  # coloured document
    cv2.imshow('gray', imgWarpGray) # gray scaled document
    cv2.imshow('scanned', imgResult) # highlighted document
    
    # press 's' to save the scanned document in the "Scanned" folder
    if cv2.waitKey(1) & 0xFF == ord('q'):

        # Prints "Scan saved" on the original image window to ensure that your scan saved
        cv2.rectangle(img, (0, 200), (480, 300), (255,0,0),cv2.FILLED)
        cv2.putText(img, "Scan Saved", (75, 265), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 255, 0), 2)
        cv2.imshow("Original", img)
        cv2.waitKey(500)
        break


    