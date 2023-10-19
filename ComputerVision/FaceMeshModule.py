import cv2 as cv
import time
import mediapipe as mp



class FaceMeshDetector():
    def __init__(self, staticMode=False, maxFaxes=2, minDetectionCon=0.5, minTrackCon=0.5):
        self.staticMode = staticMode
        self.maxFaces = maxFaxes
        self.minDetectionCon = minDetectionCon
        self.minTrackCon = minTrackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(max_num_faces=2)
        self.drawSpec = self.mpDraw.DrawingSpec(thickness = 1, circle_radius = 2)

    def findFaceMesh(self, img, draw=True):
        self.results = self.faceMesh.process(img)
        faces = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_CONTOURS, self.drawSpec, self.drawSpec)

                face = []
                for id, lm in enumerate(faceLms.landmark):
                    ih, iw, ic = img.shape
                    x ,y = int(lm.x*iw), int(lm.y*ih)
                    # print(id, x, y)
                    face.append([x,y])
            faces.append(face)
        return img, faces



def main():
    video = cv.VideoCapture('C:/Users/chris/Desktop/Dimitris/Tutorials/Videos/Video3.mp4')
    pTime = 0
    detector = FaceMeshDetector()
    while True:
        success, img = video.read()
        img = img[500:1300, 350:1700, :]
        img, faces = detector.findFaceMesh(img)
        
        if len(faces) != 0:
            print(len(faces))

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

if __name__ == "__main__":
    main()








