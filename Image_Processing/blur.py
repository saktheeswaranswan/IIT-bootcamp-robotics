import numpy as np
import cv2

#Reading an image
image = cv2.imread("joker_1.jpg", 1)

#Resinzing the image because it is huge!
image = cv2.resize(image, (500, 500))

#Blurring 
kernel = 3
blurred_img = cv2.blur(image, (kernel, kernel), 0)
blurred_img_G = cv2.GaussianBlur(image, (kernel, kernel), 0)
cv2.imshow('window', blurred_img)
cv2.imshow('window_g', blurred_img_G)
k = cv2.waitKey(0)
if k == 95:
    cv2.destroyAllWindows()
