import lgpio as sbc
from gpiozero import Motor
import time
import sys
import keyboard
from sshkeyboard import listen_keyboard



def press(key):
    # try: 
    rightMotorSpeed = 0.0
    leftMotorSpeed = 0.0
    # h = sbc.gpiochip_open(0)
    horizontalLeft = Motor(17, 27)
    horizontalRight = Motor(23, 24)

    # horizontalRight.close()
    # horizontalLeft.close()

    verticalFrontLeft = Motor(6, 5)
    # motor3.forward(.3)
    verticalFrontRight = Motor(13,12)
    # motor4.forward(.3)
    verticalBackLeft = Motor(26,16)
    # motor5.forward(.3)
    verticalBackRight = Motor(25,22)

    def moveForward(time_val, duty):
        horizontalLeft.forward(duty)
        horizontalRight.forward(duty)
        time.sleep(time_val)
        horizontalLeft.forward(0)
        horizontalRight.forward(0)
    
    def moveBackward(time_val, duty):
        horizontalLeft.backward(duty)
        horizontalRight.backward(duty)
        time.sleep(time_val)
        horizontalLeft.forward(0)
        horizontalRight.forward(0)

    def moveDown(time_val, duty):
        verticalFrontLeft.forward(duty)
        verticalFrontRight.forward(duty)
        verticalBackLeft.forward(duty)
        verticalBackRight.forward(duty)
        time.sleep(time_val)
        verticalFrontLeft.forward(0)
        verticalFrontRight.forward(0)
        verticalBackLeft.forward(0)
        verticalBackRight.forward(0)

    def moveUp(time_val, duty):
        verticalFrontLeft.backward(duty)
        verticalFrontRight.backward(duty)
        verticalBackLeft.backward(duty)
        verticalBackRight.backward(duty)
        time.sleep(time_val)
        verticalFrontLeft.backward(0)
        verticalFrontRight.backward(0)
        verticalBackLeft.backward(0)
        verticalBackRight.backward(0)

    def turnLeft(time_val, duty):
        horizontalLeft.backward(duty)
        horizontalRight.forward(duty)
        time.sleep(time_val)
        horizontalLeft.forward(0)
        horizontalRight.forward(0)

    def turnRight(time_val, duty):
        horizontalLeft.forward(duty)
        horizontalRight.backward(duty)
        time.sleep(time_val)
        horizontalLeft.forward(0)
        horizontalRight.forward(0)


    def pitchUp(time_val, duty):
        verticalFrontLeft.forward(duty)
        verticalFrontRight.forward(duty)
        verticalBackLeft.backward(duty)
        verticalBackRight.backward(duty)
        time.sleep(time_val)
        verticalFrontLeft.forward(0)
        verticalFrontRight.forward(0)
        verticalBackLeft.forward(0)
        verticalBackRight.forward(0)

    def pitchDown(time_val, duty):
        verticalFrontLeft.backward(duty)
        verticalFrontRight.backward(duty)
        verticalBackLeft.forward(duty)
        verticalBackRight.forward(duty)
        time.sleep(time_val)
        verticalFrontLeft.forward(0)
        verticalFrontRight.forward(0)
        verticalBackLeft.forward(0)
        verticalBackRight.forward(0)

    def rollLeft(time_val, duty):
        verticalFrontLeft.backward(duty)
        verticalBackLeft.backward(duty)
        verticalFrontRight.forward(duty)
        verticalFrontLeft.forward(duty)
        time.sleep(time_val)
        verticalFrontLeft.forward(0)
        verticalFrontRight.forward(0)
        verticalBackLeft.forward(0)
        verticalBackRight.forward(0)

    def rollRight(time_val, duty):
        verticalFrontLeft.forward(duty)
        verticalBackLeft.forward(duty)
        verticalFrontRight.backward(duty)
        verticalFrontLeft.backward(duty)
        time.sleep(time_val)
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
    # motor6.forward(.3)
    if (key == 'w' and rightMotorSpeed <= 0.95):
        moveForward(.2, .5)
        print(f'Forward Speed: {.5}')
        time.sleep(0.1)
    if (key == 's' and leftMotorSpeed <= 0.95):
        moveBackward(.2, .5)
        print(f'Backward Speed: {.5}')
        time.sleep(0.1)
    if (key == 'o' ):
        moveUp(.2, .5)
        print(f'Up Speed: {.5}')
        time.sleep(0.1)
    if (key == 'l'):
        moveDown(.2, .5)
        print(f'Down Speed: {.5}')
        time.sleep(0.1)
    if (key == 'i'):
        pitchUp(.2, .5)
        print("Pitch up Motor .3")
        time.sleep(0.1)
    if (key == 'p'):
        pitchDown(.2, .5)
        print("Pitch Down Motor .3")
        time.sleep(0.1)
    if (key == 'd'):
        turnRight(.2, .5)
        print("Turn Right Motor .3")
        time.sleep(0.1)
    if (key == 'a'):
        turnLeft(.2, .5)
        print("turn left Motor .3")
        time.sleep(0.1)
    if (key == 'x'):
        unlink()
        return

while(1):
    listen_keyboard(on_press = press)
    # motor3.forward(rightMotorSpeed)
    # horizontalLeft.forward(leftMotorSpeed)
    # if (keyboard.is_pressed('o') and rightMotorSpeed <= 0.95):
    #     rightMotorSpeed += 0.05
    #     print(f'Right Speed: {rightMotorSpeed}')
    #     time.sleep(0.1)
    # if (keyboard.is_pressed('w') and leftMotorSpeed <= 0.95):
    #     leftMotorSpeed += 0.05
    #     print(f'Left Speed: {leftMotorSpeed}')
    #     time.sleep(0.1)
    # if (keyboard.is_pressed('s') and leftMotorSpeed >= 0.05):
    #     leftMotorSpeed -= 0.05
    #     print(f'Left Speed: {leftMotorSpeed}')
    #     time.sleep(0.1)
    # if (keyboard.is_pressed('l') and rightMotorSpeed >= 0.05):
    #     rightMotorSpeed -= 0.05
    #     print(f'Right Speed: {rightMotorSpeed}')
    #     time.sleep(0.1)
    # if (keyboard.is_pressed('a')):
    #     horizontalLeft.reverse()
    #     print("Left Motor Reversed")
    #     time.sleep(0.1)
    # if (keyboard.is_pressed('k')):
    #     horizontalRight.reverse()
    #     print("Right Motor Reversed")
    #     time.sleep(0.1)
    # if (keyboard.is_pressed('x')):
    #     horizontalRight.close()
    #     horizontalLeft.close()
    #     break

        


    # print(h)
    # sbc.gpio_claim_output(h, 27)
    # sbc.gpio_claim_motor2.forward(.01)utput(h, 17)
    # sbc.gpio_claim_output(h, 23)
    # sbc.gpio_claim_output(h, 24)

#     for i in range(0,5):
#         print(i)
#         #motor1.reverse()
#         # motor2.reverse()
#         # sbc.tx_pwm(h,3,1000,0,0,600)
#         # sbc.tx_pwm(h,27,500,50,0,6000)
#         # sbc.tx_pwm(h,17,500,0,0,600)
#         # sbc.tx_pwm(h,27,1000,0,0,600)
#         # sbc.tx_pwm(h,24,1000,0,0,600)
        
#         time.sleep(1)
#         #motor1.reverse()
#         # motor2.reverse()
#         # sbc.tx_pwm(h,3,1000,0,0,600)
#         # sbc.tx_pwm(h,27,500,0,0,6000)
#         # sbc.tx_pwm(h,17,500,0,0,600)
#         # sbc.tx_pwm(h,27,1000,50,0,600)
#         # sbc.tx_pwm(h,24,1000,0,0,600)
#         time.sleep(1)
#         # motor2.forward(.05)
# except:
#     print('interrupted')

# finally:
#     print('made it')
#     # sbc.tx_pwm(h,27,500,0,0,600)
#     # sbc.tx_pwm(h,17,500,0,0,600)
#     # sbc.gpio_write(h,17,0)
#     # sbc.gpio_write(h,27,0)
#     # sbc.gpio_free(h,27)
#     # sbc.gpio_free(h,17)
#     # sbc.gpio_free(h,23)
#     # sbc.gpio_free(h,24)
#     # sbc.gpiochip_close(h)
#     print('boom')