#https://github.com/OlafenwaMoses/ImageAI (other option)
#https://docs.opencv.org/3.4.4/d7/d8b/tutorial_py_face_detection.html
#import librairies
from picamera import PiCamera
from time import sleep
import cv2
#import argparse
import gpiozero as gpio
import numpy

#define vars
goUpPin = 17
goDownPin = 18
imgName = "elon.png"
motorSpeed = 0.5
normalHeight =
hMidScreen =


#define functions
def take_pic():
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    sleep(2)
    camera.capture(imgName)

def process_pic():
    face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('models/haarcascade_eye.xml')
#    imgColor = cv2.imread(imgName,cv2.IMREAD_UNCHANGED)
    imgGray = cv2.imread(imgName,cv2.IMREAD_GRAYSCALE)
#    print(imgColor.shape)

#    scale_percent = 60 # percent of original size
#    width = int(imgColor.shape[1] * scale_percent / 100)
#    height = int(imgColor.shape[0] * scale_percent / 100)
#    dim = (width, height)
#    # resize image
#    imgColor = cv2.resize(imgColor, dim, interpolation = cv2.INTER_AREA)
#
#    scale_percent = 60 # percent of original size
#    width = int(imgGray.shape[1] * scale_percent / 100)
#    height = int(imgGray.shape[0] * scale_percent / 100)
#    dim = (width, height)
#    # resize image
#    imgGray = cv2.resize(imgGray, dim, interpolation = cv2.INTER_AREA)

#    print(imgColor.shape)
#    cv2.imshow('imgColor',imgColor)
#    cv2.waitKey(0)
#    cv2.imshow('imgGray',imgGray)
#    cv2.waitKey(0)
    faceArray = face_cascade.detectMultiScale(imgGray,1.3,5)
    x = faceArray[0][0]
    y = faceArray[0][1]
    w = faceArray[0][2]
    h = faceArray[0][3]
#    cv2.rectangle(imgColor, (x,y), (x+w,y+h), (255,0,0),2)                #rectangle(image,startPos,endPos,rectColor,?)
    roi_gray = imgGray[y:y+h, x:x+w]                                       #roi(Region of interrest)
#    roi_color = imgColor[y:y+h, x:x+w]
    eyesArray = eye_cascade.detectMultiScale(roi_gray)
#    for (ex,ey,ew,eh) in eyesArray:
#        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)        #rectangle(image,startPos,endPos,rectColor,?)
#    cv2.imshow('img',imgColor)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
    return faceArray,eyesArray
    
def calculate_time(faceArray,eyesArray):
    
    if faceArray == [] or eyesArray == []:
        return 0,0
    
    yFace = faceArray[0][1]
    
    if eyesArray[0][2] > eyesArray[1][2]:
        yEyes = eyesArray[0][2]
    else:
        yEyes = eyesArray[1][2]
    
    hFront = (yFace + yEyes)/2
    
    if hFront < 768/2:
        direction = 2                               # dir=2 up
    else:
        if:hFront > 768/2:
            direction = 1                           # dir=1 down
        else:
            direction = 0                           # dir=0 good
    
    time = 
    
    
    return direction,time

def move_screen(direction,time):
    if direction == 1:
        return -1
    if direction == 2:
        motor = LED(turnLeftPin)
    else:
        if direction == 2:
            motor = LED(turnRightPin)
    motor.on()
    sleep(time)
    motor.off()


#Main
while True!= 0: #TODO: change the statement
    #take_pic()
    faces,eyes = process_pic()
    print("faces array")
    print(faces)
    print("------------")
    sleep(5)
    print("eyes array")
    print(eyes)
    print("------------")
    sleep(5)
    #move_screen(caluclate_time(faces,eyes))