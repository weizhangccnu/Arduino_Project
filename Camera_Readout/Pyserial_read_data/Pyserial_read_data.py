#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import copy
import time
import serial
import struct
import socket
import winsound
import datetime
import heartrate
import numpy as np
import pyvisa as visa
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
#========================================================================================#
## plot parameters
lw_grid = 0.5                   # grid linewidth
fig_dpi = 800                   # save figure's resolution
#========================================================================================#
freqency = 1000
duration = 1000
'''
@author: Wei Zhang
@date: 2021-03-29
This script is used to receive UART data from Camera (Model: OV7670). 
'''
#========================================================================================#
def main():
    read_bytes = []
    ser = serial.Serial('COM5', baudrate=1000000, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
    print("Serial port: %s"%ser.name)
    i = 0
    while(True):
        if ser.in_waiting:
            if i < 5:
                if ser.readline(ser.in_waiting) == b'*RDY*':            # find the first "*RDY*"
                    i += 1
                    if i == 5:
                        print("Start receiving camera data...")
            elif i == 5:                                                # receive one frame camera data
                byte_str = ser.readline(ser.in_waiting)
                if (byte_str == b'*RDY*'):
                    i += 1
                else:
                    # print(byte_str)
                    read_bytes += list(byte_str)                        # store one frame camera data
            else:                                                       # break
                break

    print(len(read_bytes))
    with open("Camera_data.txt", 'w') as infile:                        # store camera data
        for i in range(len(read_bytes)):
            infile.write("%d\n"%read_bytes[i])

    x = np.reshape(read_bytes, (320, 240))                              # plot image
    plt.imshow(x, cmap='gray', vmin=0, vmax=255)
    plt.show()
#========================================================================================#
if __name__ == "__main__":
    main()