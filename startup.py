#import librairies
#from picamera import PiCamera
import time
import cv2
import argparse

# init camera uncomment when on RasPI
#camera = PiCamera()
#camera.resolution = (800, 600)
#camera.framerate = 30
#camera.capture("image.jpg")
 
# autofocus delay
time.sleep(0.5)
 
argParse = argparse.ArgumentParser()
argParse.add_argument("-i", "--image", required = True, help="Path to image")
args = vars(argParse.parse_args())

#opencv part
face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('models/haarcascade_eye.xml')

imgColor = cv2.imread(args["image"],cv2.IMREAD_UNCHANGED)
imgGray = cv2.imread(args["image"],cv2.IMREAD_GRAYSCALE)
#cv2.imshow('imgColor',imgColor)
#cv2.waitKey(0)
#cv2.imshow('imgGray',imgGray)
#cv2.waitKey(0)
faces = face_cascade.detectMultiScale(imgGray,1.3,5)
for (x,y,w,h) in faces:
    cv2.rectangle(imgColor, (x,y), (x+w,y+h), (255,0,0),2)
    roi_gray = imgGray[y:y+h, x:x+w]
    roi_color = imgColor[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imshow('img',imgColor)
cv2.waitKey(0)
cv2.destroyAllWindows()