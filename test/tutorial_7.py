import cv2 as cv
import numpy as np

def clamp(pv):
    if pv > 255:
        return 255
    if pv < 255:
        return pv
    else:
        return 0

def gaussianNoise(image):
    h, w, c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0,20,3)

            b = image[row,col,0] # blue
            g = image[row,col,1] # green
            r = image[row,col,2] # red

            image[row,col,0] = clamp(b + s[0])
            image[row,col,1] = clamp(g + s[1])
            image[row,col,2] = clamp(r + s[2])
    cv.imshow("noise image", image)

src = cv.imread("D:/opencv/head.jpg")
cv.imshow("head.jpg",src)

t1 = cv.getTickCount()
gaussianNoise(src)
t2 = cv.getTickCount()

dst = cv.GaussianBlur(src,(0,0),15)
cv.imshow("GaussianBlur",dst)

time = (t2 - t1)/cv.getTickFrequency()

print("time:",time,"s")

cv.waitKey(0)
cv.destroyAllWindows()