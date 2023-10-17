import cv2 as cv


#Reading Videos
capture = cv.VideoCapture('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/TutorialOpenCV/Resources/Videos/dog.mp4')


def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)


while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    
    # cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    # The cv.waitKey() function in OpenCV is used to wait for a specified amount of time for a keyboard event to occur. 
    # Its primary purpose is to introduce a delay between frames in video playback and to check if a specific key has been pressed. 
    # delay: This parameter represents the time in milliseconds that OpenCV should wait for a key event. If set to 0 (or a negative value), 
    # cv.waitKey(0) will wait indefinitely until a key is pressed. If set to a positive value, it will wait for that number of milliseconds 
    # and then return -1 if no key was pressed during that time.

    # The expression 0xFF == ord('d') is a comparison that checks if the ASCII code of the key 'd' is equal to the value 0xFF (255 in decimal). 
    # In the context of OpenCV and keyboard input, this comparison is typically used to check if a specific key, in this case, 'd', is pressed.
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    # In this example, the code waits for 20 milliseconds after displaying each frame. If the 'd' key is pressed during that time, 
    # the loop is exited, leading to the release of the video capture and the closing of the display window. If no key is pressed, cv.waitKey(20) returns -1, and the loop continues with the next frame.
    # cv.waitKey() is useful for controlling the pace of video playback or for introducing delays in image processing loops, 
    # where you might want to provide the user with a way to interact with the application.


capture.release()
cv.destroyAllWindows()
