import cv2 as cv
import numpy as np



def bliateralFilter(image):
    dst = cv.bilateralFilter(image,0,100,15)
    cv.imshow("bliateralFilter",dst)

def pyrMeanShiftFilter(image):
    dst = cv.pyrMeanShiftFiltering(image,10,50)
    cv.imshow("pyrMeanShiftFilter",dst)

src = cv.imread("D:/opencv/head.jpg")
cv.imshow("head.jpg",src)

bliateralFilter(src)
pyrMeanShiftFilter(src)


cv.waitKey(0)
cv.destroyAllWindows()