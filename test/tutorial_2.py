import cv2 as cv
import numpy as np

def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("height:",height,"width:",width,"channels:",channels)
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row,col,c]
                image[row,col,c] = 255 - pv
    cv.imshow("pixels_demo",image)


def create_image():
    img = np.zeros([400,400,3],np.uint8)
    cv.imshow("new image", img)
    img[:,:,0] = np.ones[400,400]*255

def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("inverse demo ",dst)

src = cv.imread("D:/opencv/head.jpg")

t1 = cv.getTickCount()
#access_pixels(src)
inverse(src)
t2 = cv.getTickCount()
print("time:",(t2-t1)/cv.getTickFrequency()*1000,"ms")

#create_image()

cv.waitKey(0)
cv.destroyAllWindows()