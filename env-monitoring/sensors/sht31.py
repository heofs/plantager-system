#! /usr/bin/env python3

import smbus
import time


class SHT31(object):
    def __init__(self):
        # Get I2C bus
        self.bus = smbus.SMBus(1)

    def read_sensor(self):
        '''
        Returns a dict with temperature in celcius and humidity in RH.\n
        Example { "t": 22.4, "rh": 55.2 }
        '''
        # SHT31 address, 0x44(68)
        # Send measurement command, 0x2C(44)
        #		0x06(06)	High repeatability measurement
        self.bus.write_i2c_block_data(0x44, 0x2C, [0x06])

        time.sleep(0.5)

        # SHT31 address, 0x44(68)
        # Read data back from 0x00(00), 6 bytes
        # Temp MSB, Temp LSB, Temp CRC, Humididty MSB, Humidity LSB, Humidity CRC
        data = self.bus.read_i2c_block_data(0x44, 0x00, 6)

        # Convert the data
        temp = data[0] * 256 + data[1]
        cTemp = -45 + (175 * temp / 65535.0)
        humidity = 100 * (data[3] * 256 + data[4]) / 65535.0

        return {"t": cTemp, "rh": humidity}

