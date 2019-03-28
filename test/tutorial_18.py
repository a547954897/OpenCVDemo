import cv2 as cv
import numpy as np

def line_detection(image):
    # 变灰
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.Canny(gray,50,150,apertureSize=3)

    cv.imshow()





src = cv.imread("D:/opencv/head.jpg")
cv.imshow("head.jpg",src)


cv.waitKey(0)
cv.destroyAllWindows()