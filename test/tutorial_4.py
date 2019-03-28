import cv2 as cv
import  numpy as np
src = cv.imread("D:/opencv/1.png")
src2 = cv.imread("D:/opencv/2.png")

def add_demo(m1,m2):
    dst = cv.add(m1,m2)
    cv.imshow("add mdemo",dst)

def subtract_demo(m1,m2):
    dst = cv.subtract(m1,m2)
    cv.imshow("add mdemo",dst)

def divide_demo(m1,m2):
    dst = cv.divide(m1,m2)
    cv.imshow("add mdemo",dst)

def multiply_demo(m1,m2):
    dst = cv.multiply(m1,m2)
    cv.imshow("add mdemo",dst)

def others(m1,m2):
    M1,dev1 = cv.meanStdDev(m1)
    M2 = cv.mean(m2)
    print("m1：",m1,"m2：",m2)
    h, w = m1.shape[:2]
    img = np.zeros([h,w],np.uint8)
    m,dev = cv.meanStdDev(img)
    print(m)
    print(dev)

def logic_demo(m1,m2):
    dst = cv.bitwise_and(m1,m2)
    cv.imshow("bit_wise",dst)


def contrast_brightness_demo(image,c,b):
    h,w,ch = image.shape
    blank = np.zeros([h,w,ch],image.dtype)
    dst = cv.addWeighted(image,c,blank,1-c,b)
    cv.imshow("con-bri-demo",dst)

# cv.imshow("one",src)
# cv.imshow("two",src2)
# logic_demo(src,src2)
src = cv.imread("D:/opencv/head.jpg")
cv.imshow("src1",src)
contrast_brightness_demo(src,2,0)
cv.waitKey(0)
cv.destroyAllWindows()

