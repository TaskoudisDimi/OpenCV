import cv2 as cv
import mediapipe as mp
import time



video = cv.VideoCapture('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/ComputerVision/Videos/Video3.mp4')
pTime = 0


mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()


while True:
    success, img = video.read()
    img = img[500:1300, 350:1700, :]
    
    # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = faceDetection.process(img)
    # print(results)

    if results.detections:
        for id, detection in enumerate(results.detections):
            mpDraw.draw_detection(img, detection)
            # print(id, detection)
            # print(detection.score)
            # print(detection.location_data.relative_bounding_box)

    

    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img, f'FPS: {int(fps)}', (20, 70), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv.imshow("Face Detection", img)
    cv.waitKey(1)




