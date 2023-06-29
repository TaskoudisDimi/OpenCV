import cv2 as cv


# img = cv.imread('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/Resources/Photos/cat.jpg')
# cv.imshow('Cat',img)
# cv.waitKey(0)

#Reading Videos
capture = cv.VideoCapture('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


