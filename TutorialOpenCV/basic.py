import cv2 as cv


img = cv.imread('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/Resources/Photos/cat.jpg')


# # Converting to grayscale
# This line converts the input image (img) from color (BGR) to grayscale. Grayscale images have a single channel
# 1) Grayscale (Single Channel):

# In a grayscale image, there is only one channel. Each pixel in the image stores a single intensity value, typically ranging from 0 (black) to 255 (white).
# The cv2.GaussianBlur function is often applied to grayscale images to reduce noise and smooth the intensity variations within the image. When applied to a grayscale image, it operates on a single channel of intensity values.
# RGB (Three Channels):

# 2) In an RGB image, there are three channels: one for Red, one for Green, and one for Blue. Each pixel is represented by a combination of these three color channels.
# The cv2.GaussianBlur function can also be used with RGB images. When applied to an RGB image, it performs the Gaussian blur independently on each of the three color channels.
# RGBA (Four Channels):

# 3) In an RGBA image, there are four channels: Red, Green, Blue, and Alpha. The Alpha channel stores transparency information.
# The cv2.GaussianBlur function can be applied to RGBA images, and it operates on all four color channels, including the transparency channel.
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Cat', gray)


# # Blur
# Gaussian blurring is often used to reduce noise in the image
# The (5, 5) argument specifies the size of the kernel (a 5x5 Gaussian kernel is used), 
# and 1 represents the standard deviation of the Gaussian distribution. 
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# # cv.imshow('Cat', blur)


# # Edge Cascade
# This line applies the Canny edge detection algorithm to the original image (img). 
# It detects edges in the image based on intensity gradients. The values 125 and 175 are the lower and upper thresholds for edge detection. 
# You can adjust these values to control the sensitivity of edge detection.
# canny = cv.Canny(blur, 125, 175)
# # cv.imshow('Cat', canny)


# # Dilating the image
# This line dilates the edges in the Canny-detected image (imgCanny) using the defined kernel. 
# Dilation thickens the edges.
# dilated = cv.dilate(canny, (7,7), iterations = 3)
# # cv.imshow('Cat', dilated)


# # Eroding
# This line erodes the dilated image (dilated) using the same kernel, which makes the edges thinner and more pronounced.
# eroded = cv.erode(dilated, (3,3), iterations = 1)
# # cv.imshow('Cat', eroded)

# The kernel is a structuring element that defines the shape and size of the neighborhood used for the morphological operations 
# (dilation and erosion). It acts as a mask that slides over the image, and the operation is applied within this neighborhood.
# The kernel defines the shape and size of the neighborhood. It is typically a square or rectangular matrix of 1s (white) and 0s (black). 
# The size of the kernel determines the size of the area considered during dilation or erosion.
# In your provided code, kernel = np.ones((5, 5)) creates a 5x5 square kernel consisting of all 1s, 
# which means that during dilation and erosion, the operation is applied in a 5x5 neighborhood.
# A larger kernel size allows for a more significant impact on the image, affecting a broader region.


# # Resize
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Cat', resized)


# # Copping
# cropped = img[50:200, 200:400]
# cv.imshow('Cat', cropped)


cv.waitKey(0)
