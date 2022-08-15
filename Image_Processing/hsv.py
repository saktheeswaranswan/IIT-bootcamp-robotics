import cv2
import numpy as np


cap = cv2.VideoCapture(0)
while True:
    return_val, frame = cap.read()
    #Converting to HSV space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([110,50,50]) #Defining lower range
    upper = np.array([130, 255, 255]) #DEfining upper limit
    mask = cv2.inRange(hsv, lower, upper) #Using the inRange function to give a binary mask
    cv2.imshow("Showing video", mask)
    cv2.imshow("Showing hsv", hsv)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break    