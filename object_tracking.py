import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    # define range of BGR color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    lower_green = np.array([50,100,100])
    upper_green = np.array([70,255,255])
    lower_red = np.array([0,100,100])
    upper_red = np.array([10,255,255])
    
    # Threshold the HSV image to get three masks colors
    mask_blue = cv.inRange(hsv, lower_blue, upper_blue)
    mask_green = cv.inRange(hsv, lower_green, upper_green)
    mask_red = cv.inRange(hsv, lower_red, upper_red)
    
    # Bitwise-AND mask and original image
    res_blue = cv.bitwise_and(frame,frame, mask= mask_blue)
    res_green = cv.bitwise_and(frame,frame, mask= mask_green)
    res_red = cv.bitwise_and(frame,frame, mask= mask_red)
    cv.imshow("frame",frame)
    cv.imshow("mask_blue",mask_blue)
    cv.imshow("res_blue",res_blue)
    cv.imshow("mask_green",mask_green)
    cv.imshow("res_green",res_green)
    cv.imshow("mask_red",mask_red)
    cv.imshow("res_red",res_red)
    
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()