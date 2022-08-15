import numpy as np
import cv2

#Reading an image
image = cv2.imread("joker_1.jpg", 0)
#Resinzing the image because it is huge!
image = cv2.resize(image, (720, 720))
#Displaying the image
cv2.imshow('window', image)
k = cv2.waitKey(0)
if k == 95:
    cv2.destroyAllWindows()