import cv2 as cv
import numpy as np


def template_demo():
    tpl = cv.imread("D:/opencv/head.jpg")






src = cv.imread("D:/opencv/head.jpg")
cv.imshow("head.jpg",src)


cv.waitKey(0)
cv.destroyAllWindows()