
import numpy as np
import cv2 as cv


def FromBGR_To_Gray(img):
    # Convert the image to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return gray


def FromGray_To_Lap(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    lap = cv.Laplacian(gray, cv.CV_64F)
    lap = np.uint8(np.absolute(lap))
    return lap


def FromGray_To_Canny(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    canny = cv.Canny(gray, 150, 175)
    return canny



def FromImage_To_Blue(img):
    # blank is initialized as a blank (black) image. It is created using NumPy with the same dimensions as the first two dimensions of the img shape. 
    blank = np.zeros(img.shape[:2], dtype='uint8')
    b,g,r = cv.split(img)
    blue = cv.merge([b,blank,blank])
    return blue

def FromImage_To_Green(img):
    # blank is initialized as a blank (black) image. It is created using NumPy with the same dimensions as the first two dimensions of the img shape. 
    blank = np.zeros(img.shape[:2], dtype='uint8')
    b,g,r = cv.split(img)
    green = cv.merge([blank,g,blank])
    return green

def FromImage_To_Red(img):
    # blank is initialized as a blank (black) image. It is created using NumPy with the same dimensions as the first two dimensions of the img shape. 
    blank = np.zeros(img.shape[:2], dtype='uint8')
    b,g,r = cv.split(img)
    red = cv.merge([blank,blank,r])
    return red


def Detect_Faces(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    haar_cascade = cv.CascadeClassifier('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/TutorialOpenCV/haar_face.xml')
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
    print(f'Number of faces found = {len(faces_rect)}')
    for (x,y,w,h) in faces_rect:
        cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
    return img




