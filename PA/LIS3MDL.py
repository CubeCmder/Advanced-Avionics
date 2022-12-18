"""
CODE TO INTERFACE WITH THE COMPASS ONBOARD THE BERRY-GPS-IMU-v4

"""
import smbus

LIS3MDL_ADDRESS = 0x1C

LIS3MDL_WHO_AM_I = 0x0F

LIS3MDL_CTRL_REG1 = 0x20

LIS3MDL_CTRL_REG2 = 0x21
LIS3MDL_CTRL_REG3 = 0x22
LIS3MDL_CTRL_REG4 = 0x23
LIS3MDL_CTRL_REG5 = 0x24

LIS3MDL_STATUS_REG = 0x27

LIS3MDL_OUT_X_L = 0x28
LIS3MDL_OUT_X_H = 0x29
LIS3MDL_OUT_Y_L = 0x2A
LIS3MDL_OUT_Y_H = 0x2B
LIS3MDL_OUT_Z_L = 0x2C
LIS3MDL_OUT_Z_H = 0x2D

LIS3MDL_TEMP_OUT_L = 0x2E
LIS3MDL_TEMP_OUT_H = 0x2F

LIS3MDL_INT_CFG = 0x30
LIS3MDL_INT_SRC = 0x31
LIS3MDL_INT_THS_L = 0x32
LIS3MDL_INT_THS_H = 0x33

class BMP388(object):
    """docstring for BMP388"""

    def __init__(self, address=I2C_ADD_BMP388):
        self._address = address
        self._bus = smbus.SMBus(0x01)