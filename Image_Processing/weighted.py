import numpy as np
import cv2


#Reading an image
apple = cv2.imread("apple.jpeg", 1)
orange = cv2.imread("orange.jpeg", 1)

#Creating a window to display the image
apple = cv2.resize(apple, (720, 720))
orange = cv2.resize(orange, (720, 720))

img_weighted = cv2.addWeighted(apple, 0.5, orange, 0.5, 0)

cv2.imshow('window', img_weighted)
k = cv2.waitKey(0)
if k == 95:
    cv2.destroyAllWindows()
