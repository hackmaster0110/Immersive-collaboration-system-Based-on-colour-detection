
# import the necessary packages

import imutils
import cv2

import Xlib
from Xlib import X,display
import Xlib.XK
import Xlib.error
import Xlib.ext.xtest
import numpy as np
d1= np.array([])
d2 = np.array([])

#file = open('cor.txt', 'w')

Lower = (0, 90, 90)
Upper = (150, 255, 255)
approx = 3
d = display.Display()


def movemouse(mx, my):
    s = d.screen()
    root = s.root
    root.warp_pointer(mx, my)
    d.sync()


def down(button):
    Xlib.ext.xtest.fake_input(d, X.ButtonPress, button)


def up(button):
    Xlib.ext.xtest.fake_input(d, X.ButtonRelease, button)

#Enter the vertex positions.

moni_resolx = 1024
moni_resoly = 768
vertix1 = 45
vertiy1 = 217
vertix2 = 457
vertiy2 = 427
cx = vertix2 - vertix1
cy = vertiy2 - vertiy1
valuex = moni_resolx / cx
valuey = moni_resoly / cy

cap = cv2.VideoCapture(0)

# keep looping
while True:
    # grab the current frame
    ret,img = cap.read()
    #resize the frame, blur it, and convert it to the HSV

    img = imutils.resize(img, width=600)
    frame=img
    #frame = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # color spacer in the mask
    mask = cv2.inRange(hsv, Lower, Upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # find contours in the mask and initialize the current

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        # only proceed if the radius meets a minimum size

        # print(center)
        if radius > 10:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            # cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)


    try:

        dx = center[0]
        dy = center[1]
        d1 = np.append(d1, dx)
        d2 = np.append(d2, dy)
        if ((len(d1)) and (len(d2))) == approx + 1:
            xmean = np.mean(d1)
            ymean = np.mean(d2)
            d1 = np.delete(d1, range(0, approx + 1))
            d2 = np.delete(d2, range(0, approx + 1))
        #file.write(str(int(xmean)) + ',' + str(int(ymean)))
        #file.close()
    # print(len(d1),len(d2))
    # print(int(xmean),int(ymean))
    # print(dx,dy)
    except:
        pass


    try:

        if ((xmean >= vertix1 and xmean <= vertix2) and (ymean >= vertiy1 and ymean <= vertiy2)):
            calix = valuex * (xmean - vertix1)
            caliy = valuey * (ymean - vertiy1)
            movemouse(int(calix), int(caliy))
    except:
        pass


    #show the frame to our screen
    #cv2.imshow("Frame", frame)

    key = cv2.waitKey(1) & 0xFF

    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

# cleanup the camera and close any open windows
cv2.destroyAllWindows()
