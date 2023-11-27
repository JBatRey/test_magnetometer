import serial
import re
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

ser = serial.Serial('COM4', 9600)

def read_serial_data():
    try:
        while ser.in_waiting > 0:        
            line = ser.readline().decode('utf-8').strip()

        match = re.match(r'X([+\-]\d+)Y([+\-]\d+)', line)
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
            return x, y
    except Exception as e:
        print(f"Error reading serial data: {e}")
    return None

fig, ax = plt.subplots()
vectors = []
scatter_points = []
quiver = ax.quiver(0, 0, 0, 0, angles='xy', scale_units='xy', scale=1, color='blue')

def update_plot(frame):
    data = read_serial_data()
    if data:
        x, y = data
        vectors.append((x, y))

        # Ensure that scatter_points has enough elements
        while len(scatter_points) < len(vectors):
            scatter_points.append(ax.scatter(0, 0, color='red', marker='.'))

        # Update existing scatter points (consider only the last 50 points)
        for vec, point in zip(vectors[-50:], scatter_points[-50:]):
            point.set_offsets([vec[0], vec[1]])

        # Update existing quiver arrow
        quiver.set_UVC(x, y)

        return scatter_points[-50:] + [quiver]

ani = FuncAnimation(fig, update_plot, blit=True, interval=60)

plt.xlim(-500, 500)
plt.ylim(-500, 500)
plt.title("2D Vector Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
