import numpy as np
import cv2


#Reading an image
image = cv2.imread("joker_1.jpg", 1)
#Resinzing the image because it is huge!
image = cv2.resize(image, (500, 500))
#Printing image shape 
print("Image shape", image.shape) #Rows, colums, channels
#See the type of the data <type 'numpy.ndarray'>
print("Type", type(image))

#BGR value at that point
BGR = image[100,30]
B = image[100, 30, 0]
G = image[100, 30, 1]
R = image[100, 30, 2]

print("BGR values at the point", BGR)
print("B values at the point", B)
print("G values at the point", G)
print("R values at the point", R)

blue, green, red = cv2.split(image)

#Displaying the image
cv2.imshow('window', image)
cv2.imshow('Blue', blue)
cv2.imshow('Green', green)
cv2.imshow('Red', red)
k = cv2.waitKey(0)
if k == 95:
    cv2.destroyAllWindows()
