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
camera = PiCamera()
goUpPin = 17
goDownPin = 18
imgName = "image.png"
motorSpeed = 0.5
taillePixel = 0.28
isScreenCorrectlyPlaced = False


#define functions
def take_pic():
    camera.resolution = (1024, 768)
    camera.start_preview()
    sleep(2)
    camera.capture(imgName)
    camera.stop_preview()

def process_pic():
    face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('models/haarcascade_eye.xml')
    imgColor = cv2.imread(imgName,cv2.IMREAD_UNCHANGED)
    imgGray = cv2.imread(imgName,cv2.IMREAD_GRAYSCALE)

    faceArray = face_cascade.detectMultiScale(imgGray,1.3,5)
    if faceArray == ():
        return [],[]
    
    x = faceArray[0][0]
    y = faceArray[0][1]
    w = faceArray[0][2]
    h = faceArray[0][3]
    
    cv2.rectangle(imgColor, (x,y), (x+w,y+h), (255,0,0),2)                #rectangle(image,startPos,endPos,rectColor,?)
    roi_gray = imgGray[y:y+h, x:x+w]                                       #roi(Region of interrest)
    roi_color = imgColor[y:y+h, x:x+w]
    eyesArray = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyesArray:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)        #rectangle(image,startPos,endPos,rectColor,?)
    cv2.imshow('img',imgColor)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return faceArray,eyesArray
    
def calculate_time(faceArray,eyesArray):
    
    if (faceArray == [] or eyesArray == []): #or eyesArray.shape == (2,3):
        return 0,0
    
    yFace = faceArray[0][1]
    
    if eyesArray[0][2] > eyesArray[1][2]:
        yEyes = eyesArray[0][2]
    else:
        yEyes = eyesArray[1][2]
    
    midFront = (yFace + yEyes)/2
    
    if midFront < 768/2:
        direction = 1                               # dir=1 up
    else:
        if midFront > 768/2:
            direction = 2                           # dir=2 down
        else:
            if midFront == 768/2:
                direction = 0                       # dir=0 good
            else:
                direction = -1
    
    time = midFront*taillePixel/motorSpeed
#    print("Time")
#    print(time)
#    print("Dir")
#    print(direction)
    
    
    return direction,time

def move_screen(direction,time):
    if time == 0:
        return -1
    else:
        if direction == 1:
            motor = gpio.LED(goUpPin)
        else:
            if direction == 2:
                motor = gpio.LED(goDownPin)
            else:
                if direction == 0:
                     isScreenCorrectlyPlaced = True
                else:
                    return -1
            
        motor.on()
        sleep(time)
        motor.off()


#Main
while isScreenCorrectlyPlaced != True:
    take_pic()
    faces,eyes = process_pic()
#    print("faces array")
#    print(faces)
#    print("------------")
#    sleep(1)
#    print("eyes array")
#    print(eyes)
#    print("------------")
#    sleep(1)
    direction,time = calculate_time(faces,eyes)
    move_screen(direction,time)