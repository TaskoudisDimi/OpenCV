import cv2 as cv
import numpy as np

frameWidth = 640
frameHeight = 480

# Initialize the webcam capture
cap = cv.VideoCapture(0)

cap.set(3, frameWidth) #property ID 3 for width
cap.set(4, frameHeight) #property ID 4 for height
cap.set(10, 150) #property ID 10 for brightness

def ImageProcessing(img):
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Apply Gaussian blur to reduce noise in the grayscale image
    #  This line applies a Gaussian blur to the grayscale image (imgGray). The (5, 5) 
    # argument specifies the size of the kernel (a 5x5 Gaussian kernel is used), 
    # and 1 represents the standard deviation of the Gaussian distribution. 
    # Gaussian blurring is often used to reduce noise in the image.
    imgBlur = cv.GaussianBlur(imgGray, (5,5), 1)
    # Apply Gaussian blur to reduce noise in the grayscale image
    # It detects edges in the image based on intensity gradients. 
    # The values 200 and 200 are the lower and upper thresholds for edge detection. 
    imgCanny = cv.Canny(img, 200, 200)
    # Define a kernel for morphological operations
    # This line defines a 5x5 kernel using NumPy, which will be used for morphological operations like dilation and erosion.
    kernel = np.ones((5,5))
    # Dilate the edges to make them thicker
    # Dilation thickens the edges
    imgDial = cv.dilate(imgCanny, kernel, iterations=2)
    # Erode the dilated image to make the edges thinner and more pronounced
    # This line erodes the dilated image (imgDial) using the same kernel, which makes the edges thinner and more pronounced.
    imgThres = cv.erode(imgDial, kernel, iterations=1)

    return imgThres
    

while True:
    # Capture a frame
    ret, img = cap.read()
    cv.resize(img, (frameWidth, frameHeight))
    imgThress = ImageProcessing(img)
    # Display the captured frame
    cv.imshow('Webcam Capture', imgThress)


    # Break the loop when the user presses the 'q' key
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
cap.release()
cv.destroyAllWindows()