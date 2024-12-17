import lgpio as sbc
from gpiozero import Motor
import time
import board
import adafruit_lsm9ds1
import time
import sys
import keyboard
from vision.testudo_object_detection import init_camera, detectTestudo
from sensing.test_imu import init_imu, read_imu
import torch

horizontalRight = Motor(17, 27)
horizontalLeft = Motor(24, 23)
verticalFrontRight = Motor(6, 5)
verticalFrontLeft = Motor(13,12)
verticalBackRight = Motor(26,16)
verticalBackLeft = Motor(25,22)
num_frames = 15
picam2 , model = init_camera()
imu = init_imu()
camera_angle = 75
img_center_x = 640
img_center_y = 360
img_width = 1280
img_height = 720
def main():
    boxes = []
    counter = 0
    while(len(boxes) == 0):
        print('Searching for Testudo')
        for i in range(num_frames):
            results, boxes = detectTestudo(picam2, model)
            if len(boxes) > 0:
                break
        # Turn by angle of camera
        if len(boxes) > 0:
            break       
        counter += 1
        if counter*camera_angle >= 360:
            counter = 0
            moveUp()
    xywh_coords = results.boxes.xywh
    x_center = xywh_coords[0][0]
    y_center = xywh_coords[0][1]
    x_dist = x_center - img_center_x
    y_dist = y_center - img_center_y

    alignTestudo(x_dist, x_center, img_center_x, y_dist, y_center, img_center_y, picam2, model)

    while(checkObjective(xywh_coords)):
        moveForward(.2, .15)
        alignTestudo(x_dist, x_center, img_center_x, y_dist, y_center, img_center_y, picam2, model)

        return
    
def checkObjective(xywh_coords):
    width = xywh_coords[0][2]
    height = xywh_coords[0][3]
    if width > .9*img_width or height > .9*img_height:
        return False


    return True

def alignTestudo(x_dist, x_center, img_center_x, y_dist, y_center, img_center_y, picam2, model):
    while x_dist < -30 and x_dist > 30 and y_dist < -30 and y_dist > 30:
        if x_dist < -30 or x_dist > 30:
            alignX(x_dist, x_center, img_center_x, picam2, model)
        if y_dist < -30 or y_dist > 30:
            alignY(y_dist, y_center, img_center_y, picam2, model)

def alignX(x_dist, x_center, img_center_x, picam2, model):
    while x_dist < -30:
        turnLeft(.2, .15*abs(x_dist)/30)
        for i in range(num_frames):
            results, boxes = detectTestudo(picam2, model)
            if len(boxes) > 0:
                break
        xywh_coords = results.boxes.xywh
        x_center = xywh_coords[0][0]
        x_dist = x_center - img_center_x
    while x_dist > 30:
        turnRight(.2, .15*abs(x_dist)/30)
        for i in range(num_frames):
            results, boxes = detectTestudo(picam2, model)
            if len(boxes) > 0:
                break
        xywh_coords = results.boxes.xywh
        x_center = xywh_coords[0][0]
        x_dist = x_center - img_center_x
    
def alignY(y_dist, y_center, img_center_y, picam2, model):
    while y_dist < -30:
        moveDown(.2, .15*abs(y_dist)/30)
        for i in range(num_frames):
            results, boxes = detectTestudo(picam2, model)
            if len(boxes) > 0:
                break
        xywh_coords = results.boxes.xywh
        y_center = xywh_coords[0][1]
        y_dist = y_center - img_center_y
    while y_dist > 30:
        moveUp(.2, .15*y_dist/30)
        for i in range(num_frames):
            results, boxes = detectTestudo(picam2, model)
            if len(boxes) > 0:
                break
        xywh_coords = results.boxes.xywh
        y_center = xywh_coords[0][1]
        y_dist = y_center - img_center_y


def moveForward(time, duty):
    horizontalLeft.forward(duty)
    horizontalRight.forward(duty)
    time.sleep(time)
    horizontalLeft.forward(0)
    horizontalRight.forward(0)
    
def moveBackward(time, duty):
    horizontalLeft.backward(duty)
    horizontalRight.backward(duty)
    time.sleep(time)
    horizontalLeft.forward(0)
    horizontalRight.forward(0)

def moveDown(time, duty):
    verticalFrontLeft.forward(duty)
    verticalFrontRight.forward(duty)
    verticalBackLeft.forward(duty)
    verticalBackRight.forward(duty)
    time.sleep(time)
    verticalFrontLeft.forward(0)
    verticalFrontRight.forward(0)
    verticalBackLeft.forward(0)
    verticalBackRight.forward(0)

def moveUp(time, duty):
    verticalFrontLeft.backward(duty)
    verticalFrontRight.backward(duty)
    verticalBackLeft.backward(duty)
    verticalBackRight.backward(duty)
    time.sleep(time)
    verticalFrontLeft.backward(0)
    verticalFrontRight.backward(0)
    verticalBackLeft.backward(0)
    verticalBackRight.backward(0)

def turnLeft(time, duty):
    horizontalLeft.backward(duty)
    horizontalRight.forward(duty)
    time.sleep(time)
    horizontalLeft.forward(0)
    horizontalRight.forward(0)

def turnRight(time, duty, imu, imu_check, imu_output):
    horizontalLeft.forward(duty)
    horizontalRight.backward(duty)
    time.sleep(time)
    if imu_check:
        accel, mag, gyro, temp = read_imu(imu)
    horizontalLeft.forward(0)
    horizontalRight.forward(0)
    return accel, mag, gyro, temp

def pitchUp(time, duty):
    verticalFrontLeft.forward(duty)
    verticalFrontRight.forward(duty)
    verticalBackLeft.backward(duty)
    verticalBackRight.backward(duty)
    time.sleep(time)
    verticalFrontLeft.forward(0)
    verticalFrontRight.forward(0)
    verticalBackLeft.forward(0)
    verticalBackRight.forward(0)

def pitchDown(time, duty):
    verticalFrontLeft.backward(duty)
    verticalFrontRight.backward(duty)
    verticalBackLeft.forward(duty)
    verticalBackRight.forward(duty)
    time.sleep(time)
    verticalFrontLeft.forward(0)
    verticalFrontRight.forward(0)
    verticalBackLeft.forward(0)
    verticalBackRight.forward(0)

def rollLeft(time, duty):
    verticalFrontLeft.backward(duty)
    verticalBackLeft.backward(duty)
    verticalFrontRight.forward(duty)
    verticalFrontLeft.forward(duty)
    time.sleep(time)
    verticalFrontLeft.forward(0)
    verticalFrontRight.forward(0)
    verticalBackLeft.forward(0)
    verticalBackRight.forward(0)

def rollRight(time, duty):
    verticalFrontLeft.forward(duty)
    verticalBackLeft.forward(duty)
    verticalFrontRight.backward(duty)
    verticalFrontLeft.backward(duty)
    time.sleep(time)
    verticalFrontLeft.forward(0)
    verticalFrontRight.forward(0)
    verticalBackLeft.forward(0)
    verticalBackRight.forward(0)

def unlink():
    horizontalLeft.close()
    horizontalRight.close()
    verticalFrontLeft.close()
    verticalFrontRight.close()
    verticalBackLeft.close()
    verticalBackRight.close()