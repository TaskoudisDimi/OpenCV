
import cv2 as cv


img = cv.imread('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/TutorialOpenCV/Resources/Photos/group1.jpg')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray People', gray)

haar_cascade = cv.CascadeClassifier('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/TutorialOpenCV/haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')


for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)


cv.imshow('Faces', img)



cv.waitKey(0)



