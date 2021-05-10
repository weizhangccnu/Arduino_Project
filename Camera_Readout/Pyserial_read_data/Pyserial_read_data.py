#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import copy
import time
import math
import serial
import struct
import socket
import datetime
import numpy as np
import pyvisa as visa
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
plt.rcParams['font.family'] = "Times New Roman"
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
    Start_Frame = 5
    try:
        ser = serial.Serial('COM5', baudrate=1000000, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
    except:
        ser = serial.Serial('/dev/tty.usbmodem144101', baudrate=1000000, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
    print("Serial port: %s"%ser.name)
    i = 0
    while(True):
        if ser.in_waiting:
            if i < Start_Frame:
                if ser.readline(ser.in_waiting) == b'*RDY*':            # find the first "*RDY*"
                    i += 1
                    if i == Start_Frame:
                        print("Start receiving camera data...")
            elif i == Start_Frame:                                                # receive one frame camera data
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
            x = math.floor(i/320)
            y = math.floor(i%320)
            # print(i, x, y)
            infile.write("%3d %3d %3d\n"%(x, y, read_bytes[i]))

    x = np.reshape(read_bytes, (240, 320))                              # plot image
    plt.imshow(x, cmap='gray', vmin=0, vmax=255)
    plt.savefig("Recovered_Image.pdf", orientation='landscape', dpi=fig_dpi, bbox_inches='tight')         # save figure
    plt.clf()
#========================================================================================#
if __name__ == "__main__":
    main()
