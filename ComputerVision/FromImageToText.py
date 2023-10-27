import numpy as np
import pandas as pd
import os 
import pytesseract
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image

# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


img = cv.imread('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/ComputerVision/Images/test.png')

custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, config=custom_config)
print(text)

# # make a copy of this image to draw in
# image_copy = img.copy()
# # the target word to search for
# target_word = "Item"
# # get all data from the image
# data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
# print(data.keys())



# # get all occurences of the that word
# word_occurences = [ x for x, word in enumerate(data["text"]) if word == target_word ]
# word_occurences


# for occ in word_occurences:
#     # extract the width, height, top and left position for that detected word
#     x = data["left"][occ]
#     y = data["top"][occ]
#     w = data["width"][occ]
#     h = data["height"][occ]
#     # draw the rectangular:
#     image_copy = cv2.rectangle(image_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
# plt.imsave('all_item_word.png', image_copy)
# plt.figure(figsize=(15,20))
# plt.imshow(image_copy)
# plt.show()
# #cv2.waitKey(0)

# image_all= img.copy()
# n_boxes = len(data['text'])
# for i in range(n_boxes):
#     # extract the width, height, top and left position for that detected word
#     x = data["left"][i]
#     y = data["top"][i]
#     w = data["width"][i]
#     h = data["height"][i]
#     # draw the rectangular:
#     image_all = cv2.rectangle(image_all, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
# plt.imsave('image_all.png', image_all)
# plt.figure(figsize=(15,20))
# plt.imshow(image_all)
# plt.show()


# import cv2
# import pytesseract

# img = cv2.imread('../input/invoice/invoice.png')

# h, w, c = img.shape
# boxes = pytesseract.image_to_boxes(img) 
# for b in boxes.splitlines():
#     b = b.split(' ')
#     img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
# plt.figure(figsize=(15,20))
# plt.imshow(img)
# plt.show()



# custom_config = r'--oem 3 --psm 6 outputbase digits'
# num= pytesseract.image_to_string(img, config=custom_config)
# print(num)


# custom_config = r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz --psm 6'
# text = pytesseract.image_to_string(img, config=custom_config)
# print(text)
