import cv2 as cv
import numpy as np

# 均值模糊
def blur(image):
    dst = cv.blur(image,( 2, 50))
    cv.imshow("head.jpg", dst)

def medianBlur(image):
    dst = cv.medianBlur(image,9)
    cv.imshow("medianBlur",dst)

def customBlur(image):
    kernel = np.ones([5,5],np.float32)/25
    dst = cv.filter2D(image,-1,kernel=kernel)
    cv.imshow("customBlur",dst)

src = cv.imread("D:/opencv/head.jpg")

cv.imshow("src",src)
customBlur(src)


cv.waitKey(0)
cv.destroyAllWindows()