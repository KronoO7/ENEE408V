import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
p = GPIO.PWM(7, 100)
p.start(0)

GPIO.output(3, True)
GPIO.output(5, False)

p.ChangeDutyCycle(25)

GPIO.output(7, True)

sleep(5)

GPIO.output(7, False)
GPIO.output(3, False)
GPIO.output(5, True)

p.ChangeDutyCycle(50)

GPIO.output(7, True)

sleep(5)

GPIO.output(7, False)

p.stop()

GPIO.cleanup()
