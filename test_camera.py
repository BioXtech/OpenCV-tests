import cv2
import numpy

def process_pic(img):
    face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('models/haarcascade_eye.xml')
#    cv2.imshow("test",img)
#    cv2.waitKey(0)
#    cv2.destroyWindow("test")
    imgColor = cv2.imread(img,cv2.IMREAD_UNCHANGED)
    imgGray = cv2.imread(img,cv2.IMREAD_GRAYSCALE)

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
#    cv2.imshow('img',imgColor)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
    return imgColor,faceArray,eyesArray

cv2.namedWindow("preview")
camera = cv2.VideoCapture(0)

if camera.isOpened(): # try to get the first frame
    rval, frame = camera.read()
    print("Width : ",camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    print("Height : ",camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
else:
    rval = False

while rval:
    img = process_pic(frame)
    cv2.imshow("preview", img)
    rval, frame = camera.read()
    key = cv2.waitKey(cv2.CAP_PROP_FPS)
    if key == 27: # exit on ESC
        break
camera.release()
cv2.destroyWindow("preview")