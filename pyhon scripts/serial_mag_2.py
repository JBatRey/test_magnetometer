import serial
import re
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def read_serial_port(port='COM3', baud_rate=9600):
    try:
        ser = serial.Serial(port, baud_rate)
        print(f"Reading from {port}...")

        fig, ax = plt.subplots()

        def update_plot(frame):

            while ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()

            # Use regular expression to extract X and Y coordinates
            match = re.match(r'X([+\-]\d+)Y([+\-]\d+)', line)

            if match:
                x = int(match.group(1))
                y = int(match.group(2))
                ax.clear()  # Clear the previous plot
                ax.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='blue')
                ax.set_xlim(-500, 500)
                ax.set_ylim(-500, 500)
                ax.set_title("2D Vector Plot")
                ax.set_xlabel("X-axis")
                ax.set_ylabel("Y-axis")
                ax.grid(True)
                plt.draw()

        ani = FuncAnimation(fig, update_plot, interval=100)

        plt.show()

    except serial.SerialException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    read_serial_port()
