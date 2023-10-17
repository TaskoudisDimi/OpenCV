
import cv2 as cv
import mediapipe as mp
import time
import FaceDetectionModule as detectorFace





def main():
    video = cv.VideoCapture('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/ComputerVision/Videos/Video3.mp4')
    pTime = 0
    detector = detectorFace.FaceDetector()
    while True:
        success, img = video.read()
        img = img[500:1300, 350:1700, :]
        img, bboxs = detector.findFaces(img)

        # It calculates the time difference between the current time (cTime) and the time from the previous frame (pTime) using the formula cTime - pTime. This time difference represents how long it took to process the frame.
        # It calculates the FPS by taking the reciprocal (1 divided by the time difference):
        cTime = time.time()
        # The newly calculated FPS value is then assigned to the fps variable.
        # The pTime variable is updated to the current time to be used in the next frame iteration:
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv.putText(img, f'FPS: {int(fps)}', (20, 70), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv.imshow("Face Detection", img) 
        cv.waitKey(1)



if __name__ == "__main__":
    main()

