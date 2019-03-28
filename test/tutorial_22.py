import cv2 as cv
import numpy as np

def erode_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    dst = cv.erode(binary, kernel)
    cv.imshow("erode_demo", dst)

def dilate_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    dst = cv.dilate(binary, kernel)
    cv.imshow("dilate_demo", dst)


src = cv.imread("D:/opencv/head.jpg")
cv.imshow("head.jpg",src)
erode_demo(src)
dilate_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()