import cv2 as cv
import numpy as np
def fill_color_demo(image):
    copyImg = image.copy()
    h,w = image.shape[:2]
    mask = np.zeros([h+2,w+2],np.uint8)
    cv.floodFill(copyImg,mask,(30,30),(0,255,255),(100,100,100),(50,50,50),cv.FLOODFILL_FIXED_RANGE);
    cv.imshow("fill_color_demo",copyImg)



src = cv.imread("D:/opencv/head.jpg")
fill_color_demo(src)
cv.imshow("head.jpg",src)

"""
face = src[100:500,100:500]
gray = cv.cvtColor(face,cv.COLOR_BGR2GRAY)
backface = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
src[100:500,100:500] = backface

cv.imshow("face",src)

"""

cv.waitKey(0)
cv.destroyAllWindows()