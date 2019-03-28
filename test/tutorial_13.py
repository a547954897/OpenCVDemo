import cv2 as cv
import numpy as np


def threshold_demo(image):
    # 转化成黑白图像
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)

    # 图像二值化
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    print("threshold value",ret)
    cv.imshow("binary",binary)

def local_threshold(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,25,10)
    cv.imshow("binary2",binary)

def template_demo():
    tpl = cv.imread("D:/opencv/head.jpg")






src = cv.imread("D:/opencv/head.jpg")
cv.imshow("head.jpg",src)
threshold_demo(src)
local_threshold(src)

cv.waitKey(0)
cv.destroyAllWindows()