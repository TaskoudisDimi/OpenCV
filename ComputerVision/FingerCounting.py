import cv2 as cv
import time
import os
import HandTrackingModule as track



video = cv.VideoCapture('C:/Users/chris/Desktop/Dimitris/Tutorials/Videos/Video3.mp4')
pTime = 0


folderPath = "C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/ComputerVision/Images/"
myList = os.listdir(folderPath)
print(myList)

overlayList = []

for imPath in myList:
    image = cv.imread(f'{folderPath}/{imPath}')
    print(image.shape)
    overlayList.append(image)


detector = track.handDetector()

tipIds = [4, 8, 12, 16, 20]


while True:
    success, img = video.read()
    img = img[500:1300, 350:1700, :]
    detector.findHands(img)

    lmList = detector.findPosition(img, draw=False)
    
    if len(lmList) != 0:
        fingers = []
        
        #Thump
        if lmList[tipIds[0]][1] > lmList[tipIds[0] -1][1]:
            fingers.append(1) 
        else:
            fingers.append(0)
        
        # 4 Fingers
        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1) 
            else:
                fingers.append(0)

        totalFingers = fingers.count(1)
        # print(totalFingers)

        h, w, c = overlayList[totalFingers-1].shape
        img[0:h, 0:w] = overlayList[totalFingers-1]

        cv.rectangle(img, (20, 225), (170, 524), (0,255,0), cv.FILLED)
        cv.putText(img, str(totalFingers), (45, 375), cv.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)



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



