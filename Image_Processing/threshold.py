import numpy as np
import cv2

#Reading an image
image = cv2.imread("joker_1.jpg", 1)
#Resinzing the image because it is huge!
image = cv2.resize(image, (500, 500))

#Converting to grayscale and thresholding of all types
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)

#Adaptive threshold
adaptive_thresh1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
adaptive_thresh2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow('Gray', gray)
cv2.imshow('THRESH_BINARY', thresh1)
cv2.imshow('THRESH_BINARY_INV', thresh2)
cv2.imshow('THRESH_TRUNC', thresh3)
cv2.imshow('THRESH_TOZERO', thresh4)
cv2.imshow('THRESH_TOZERO_INV', thresh5)
cv2.imshow('ADAPTIVE_MEAN', adaptive_thresh1)
cv2.imshow('ADAPTIVE_GAUSSIAN', adaptive_thresh2)

k = cv2.waitKey(0)
if k == 95:
    cv2.destroyAllWindows()