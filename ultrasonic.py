import serial
from time import sleep
print('Hello1')
ser = serial.Serial("/dev/ttyAMA10", 115200)
print('Hello')
while True:
    print('Hello2')

    recieved_data = ser.read()
    print('Hello')

    sleep(.03)
    data_left = ser.in_waiting()
    recieved_data += ser.read(data_left)
    print(recieved_data)