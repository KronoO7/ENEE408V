# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the LSM9DS1 accelerometer, magnetometer, gyroscope.
# Will print the acceleration, magnetometer, and gyroscope values every second.
import time
import board
import adafruit_lsm9ds1

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)


def init_imu():
    # Create sensor object, communicating over the board's default I2C bus
    i2c = board.I2C()  # uses board.SCL and board.SDA
    # i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
    sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)
    return sensor
# SPI connection:
# from digitalio import DigitalInOut, Direction
# spi = board.SPI()
# csag = DigitalInOut(board.D5)
# csag.direction = Direction.OUTPUT
# csag.value = True
# csm = DigitalInOut(board.D6)
# csm.direction = Direction.OUTPUT
# csm.value = True
# sensor = adafruit_lsm9ds1.LSM9DS1_SPI(spi, csag, csm)

# Main loop will read the acceleration, magnetometer, gyroscope, Temperature
# values every second and print them out.

def read_imu(sensor):
    accel_x, accel_y, accel_z = sensor.acceleration
    accel = [accel_x, accel_y, accel_z]
    mag_x, mag_y, mag_z = sensor.magnetic
    mag = [mag_x, mag_y, mag_z]
    gyro_x, gyro_y, gyro_z = sensor.gyro
    gyro = [gyro_x, gyro_y, gyro_z]
    temp = sensor.temperature
    return accel, mag, gyro, temp

# while True:
#     # Read acceleration, magnetometer, gyroscope, temperature.
#     accel, mag, gyro, temp = read_imu(sensor)
#     # Print values.
#     print(
#         "Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})".format(
#             accel[0], accel[1], accel[2]
#         )
#     )
#     print(
#         "Magnetometer (gauss): ({0:0.3f},{1:0.3f},{2:0.3f})".format(mag[0], mag[1], mag[2])
#     )
#     print(
#         "Gyroscope (rad/sec): ({0:0.3f},{1:0.3f},{2:0.3f})".format(
#             gyro[0], gyro[1], gyro[2]
#         )
#     )
#     print("Temperature: {0:0.3f}C".format(temp))
#     # Delay for a second.
#     time.sleep(.5)
