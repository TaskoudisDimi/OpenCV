import numpy as np
import cv2 as cv


haar_cascade = cv.CascadeClassifier('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/TutorialOpenCV/haar_face.xml')


# features = np.load('features.npy')
# labels = np.load('labels.npy')



people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/TutorialOpenCV/face_trained.yml')



img = cv.imread(r'C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/Resources/Faces/train/Ben Afflek/2.jpg')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)


faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
print(faces_rect)


for(x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)


