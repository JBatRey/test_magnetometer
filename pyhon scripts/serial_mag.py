import serial
import re
import os

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def read_serial_port(port='COM3', baud_rate=9600):
    x,y = 0,0
    try:
        ser = serial.Serial(port, baud_rate)
        print(f"Reading from {port}...")

        line = ser.readline().decode('utf-8').strip()
        match = re.match(r'X([+\-]\d+)Y([+\-]\d+)', line)
        
        if match:
            os.system('cls' if os.name == 'nt' else 'clear')
            x = int(match.group(1))
            y = int(match.group(2))

            
        else:
            print("Invalid format. Skipping line:", line)

    except serial.SerialException as e:
        print(f"Error: {e}")

    return x,y


if __name__ == "__main__":
    while True:
        x,y =read_serial_port()
        print(f"X: {x}, Y: {y}")