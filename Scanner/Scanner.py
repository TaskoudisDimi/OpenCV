import cv2 as cv
import numpy as np

frameWidth = 640
frameHeight = 480

# Initialize the webcam capture
# cap = cv.VideoCapture(0)

# cap.set(3, frameWidth) #property ID 3 for width
# cap.set(4, frameHeight) #property ID 4 for height
# cap.set(10, 150) #property ID 10 for brightness

def preProcessing(img):
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
    
def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 500:
            # cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.002*peri, True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 20)
    return biggest


def getWarp(img, biggest):
    pass

while True:
    # Capture a frame
    img = cv.imread('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/Scanner/Resources/paper.jpg')
    # ret, img = cap.read()
    img = cv.resize(img, (640, 480))
    imgContour = img.copy()

    imgThres = preProcessing(imgContour)
    biggest = getContours(imgThres)
    # Display the captured frame
    getWarp(img, biggest)

    cv.imshow('Webcam Capture', imgContour)


    # Break the loop when the user presses the 'q' key
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
# cap.release()
cv.destroyAllWindows()