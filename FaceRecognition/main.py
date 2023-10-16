import cv2 as cv
import numpy as np

frameWidth = 640
frameHeight = 480

# Initialize the webcam capture
cap = cv.VideoCapture(0)

cap.set(3, frameWidth) #property ID 3 for width
cap.set(4, frameHeight) #property ID 4 for height
cap.set(10, 150) #property ID 10 for brightness



while True:
    # Capture a frame
    ret, img = cap.read()
    cv.resize(img, (frameWidth, frameHeight))

    # Display the captured frame
    cv.imshow('Webcam Capture', img)


    # Break the loop when the user presses the 'q' key
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
cap.release()
cv.destroyAllWindows()