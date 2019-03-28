import cv2 as cv
import numpy as np

def video_demo():
    capture = cv.VideoCapture(0)
    while(True):
        ret,frame = capture.read()
        frame = cv.flip(frame,1)
        cv.imshow("video",frame)
        c = cv.waitKey(50)
        if c == 27:
            break

def get_image_info(image):
    print(type(image))
    print("参数、通道",image.shape)
    print("大小",image.size)
    print("类型",image.dtype)
    print(np.array(src))

src = cv.imread("D:/opencv/head.jpg")

cv.imshow("head.jpg",src)
get_image_info(src)
cv.imwrite("D:/opencv/save.png",src)

video_demo()

cv.waitKey(0)


cv.destroyAllWindows()