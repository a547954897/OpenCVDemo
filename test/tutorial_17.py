import cv2 as cv
import numpy as np

def edge_demo(image):
    blurred = cv.GaussianBlur(image,(3,3),0)
    gray = cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)

    # x Grodient
    xgrad = cv.Sobel(gray,cv.CV_16SC1,1,0)

    # y Grodient
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)

    edge_outuput = cv.Canny(gray,50,150)
    edge_outuput2 = cv.Canny(image,50,150)
    cv.imshow("canner",edge_outuput)
    cv.imshow("canner2",edge_outuput2)








src = cv.imread("D:/opencv/head.jpg")
cv.imshow("head.jpg",src)

edge_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()