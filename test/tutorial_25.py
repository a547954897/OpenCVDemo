import cv2 as cv
import numpy as np

def watershed_demo(image):
    print(image.shape)
    blurred = cv.pyrMeanShiftFiltering(image, 10, 100)
    # gray\binary image
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255,cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary-image",binary)

    #morphology operotion
    kernel = cv.getStructuringElement(cv.MORPH_RECT,( 3, 3))
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel ,iterations=2)
    sure_bg = cv.dilate(mb, kernel, iterations=3)
    cv.imshow("mor-opt ",sure_bg)




src = cv.imread("D:/opencv/head.jpg")
cv.imshow("head.jpg",src)

watershed_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()