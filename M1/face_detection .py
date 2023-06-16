#!/usr/bin/python2.7
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img= cap.read()
#    img = cv2.imread('DZcijIiW0AE0bwc.jpg') #this line to do it with a photo instead of webcam
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        
    cv2.imshow('Face recognition',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:	#ESC key 
        break

cap.release()
cv2.destroyAllWindows()
