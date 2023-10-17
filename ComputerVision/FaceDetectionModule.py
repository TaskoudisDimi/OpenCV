
import cv2 as cv
import mediapipe as mp
import time


class FaceDetector():
    def __init__(self, minDetection=0.5):
        self.minDetection = minDetection
        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(0.75)

    def findFaces(self, img, draw=True):
        self.results = self.faceDetection.process(img)
        bboxs = []
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                # print("id is:", id,"detection is " , detection)
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin *ih), \
                    int(bboxC.width * iw), int(bboxC.height * ih)
                bboxs.append([id, bbox, detection.score])
                cv.rectangle(img, bbox, (255, 0, 255), 2)
                cv.putText(img, f'{int(detection.score[0] * 100)}%', (bbox[0], bbox[1] - 20), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
        return img, bboxs


