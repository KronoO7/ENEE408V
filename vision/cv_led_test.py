import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
# from picamera2 import PiCamera2
from time import sleep

# cam = PiCamera2()
# cam.start_preview()

sleep(5)

img = cv.imread('/home/team_usa/enee408v/vision/selfie.jpg')

# print(type(img))

blur = cv.blur(img,(5,5))
blur0=cv.medianBlur(blur,5)
blur1= cv.GaussianBlur(blur0,(5,5),0)
blur2= cv.bilateralFilter(blur1,9,75,75)
hsv = cv.cvtColor(blur2, cv.COLOR_BGR2HSV)
low_blue = np.array([105, 20, 20])
high_blue = np.array([130, 255, 255])
mask = cv.inRange(hsv, low_blue, high_blue)
res = cv.bitwise_and(img,img, mask= mask)

cv.imwrite("result.jpg", res)
