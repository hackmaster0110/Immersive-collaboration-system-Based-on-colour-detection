import cv2
import numpy as np
import imutils

# mouse callback function
import imutils
cap=cv2.VideoCapture(0)
tx=0
while tx!=50:
    _,img1=cap.read()
    tx=tx+1

img1=cv2.cvtColor(img1,cv2.COLOR_RGB2BGR)
def draw_circle(event,x,y,flags,param):

    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),2,(25,200,100),-1)
        print(x,y)
img=imutils.resize(img1,width=600)
cv2.imshow('image',img)
cv2.setMouseCallback('image',draw_circle)
while True:
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
