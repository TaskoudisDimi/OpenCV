import cv2 as cv
import time
import mediapipe as mp


# video = cv.VideoCapture('C:/Users/chris/Desktop/Dimitris/Tutorials/Videos/Video3.mp4')
video = cv.VideoCapture(0)
pTime = 0

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpec = mpDraw.DrawingSpec(thickness = 1, circle_radius = 2)

while True:
    success, img = video.read()
    # img = img[500:1300, 350:1700, :]
    results = faceMesh.process(img)
    if results.multi_face_landmarks:
        for face in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, face, mpFaceMesh.FACEMESH_CONTOURS, drawSpec, drawSpec)


        for id, lm in enumerate(face.landmark):
            ih, iw, ic = img.shape
            x ,y = int(lm.x*iw), int(lm.y*ih)
            print(id, x, y)
            

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








