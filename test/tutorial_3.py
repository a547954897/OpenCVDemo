import cv2 as cv
import numpy as np




def extrace_object_demo():
    capture = cv.VideoCapture("D:/opencv/hhh.mp4")
    while(True):
        ret, frame = capture.read()
        if ret == False:
            break;

        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        lower_hsv = np.array([11,43,46])
        upper_hsv = np.array([25,255,255])

        mask = cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)

        dst = cv.bitwise_and(frame,frame,mask=mask)

        cv.imshow("video",frame)
        cv.imshow("dst",dst)
        cv.imshow("mask",mask)
        c = cv.waitKey(40)
        if c == 27:
            break

src = cv.imread("D:/opencv/head.jpg")
# cv.imshow("head.jpg",src)


cv.waitKey(0)



cv.destroyAllWindows()