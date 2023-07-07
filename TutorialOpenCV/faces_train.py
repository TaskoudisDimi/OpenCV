import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os


people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
dir = r'C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/Resources/Faces/train/'


haar_cascade = cv.CascadeClassifier('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/TutorialOpenCV/haar_face.xml')


labels = []
features = []


def create_terain():
    for person in people:
        path = os.path.join(dir, person)

        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for(x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_terain()

print(f'Length of features {len(features)}')
print(f'Length of labels {len(labels)}')

print('Training done -------------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features, labels)

face_recognizer.save('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/TutorialOpenCV/face_trained.yml')

np.save('features.npy',features)
np.save('labels.npy',labels)









