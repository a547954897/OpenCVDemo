import cv2 as cv
import numpy as np








src = cv.imread("D:/opencv/head.jpg")
cv.imshow("head.jpg",src)


cv.waitKey(0)
cv.destroyAllWindows()