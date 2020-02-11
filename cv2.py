#Importing lib
import cv2
import numpy as np

# Importing image
image = cv2.imread("jass.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

#Accessing a pixel in an image
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))

#Slicing an image 
'''roi = image[30:130, 250:350]
cv2.imshow("ROI", roi)
cv2.waitKey(0)'''

#Resizing an image
resized = cv2.resize(image, (200, 200))
cv2.imshow("Fixed Resizing", resized)
cv2.waitKey(0)

# Resizing wrt to the aspect ratio
r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resize", resized)
cv2.waitKey(0)

# Automated resizing with Imutils
resized = imutils.resize(image, width=300)
cv2.imshow('imi resize', resized)
cv2.waitKey(0)
