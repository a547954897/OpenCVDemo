import cv2 as cv
import numpy as np


def top_hat_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # 结构元素
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, kernel)
    cimage = np.array(gray.shape, np.uint8)
    cimage = 120
    cv.add(dst, cimage)
    cv.imshow("tophat",dst)





src = cv.imread("D:/opencv/head.jpg")
cv.imshow("head.jpg",src)
top_hat_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()