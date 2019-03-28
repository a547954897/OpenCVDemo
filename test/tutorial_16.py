import cv2 as cv
import numpy as np


def laplian_demo(image):
    dst = cv.Laplacian(image,cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("lapalian_demo",lpls)

def sobel_demo(image):
    # 增强
    # grad_xd = cv.Scarr(image, cv.CV_32F, 1, 0)

    grad_x = cv.Sobel(image,cv.CV_32F,1,0)
    grad_y = cv.Sobel(image,cv.CV_32F,0,1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("gradient-x",gradx)
    cv.imshow("gradient-y",grady)

    gradxy = cv.addWeighted(gradx,0.5,grady,0.5,0)
    cv.imshow("gradxy",gradxy)







src = cv.imread("D:/opencv/head.jpg")
cv.imshow("head.jpg",src)

laplian_demo(src)


cv.waitKey(0)
cv.destroyAllWindows()