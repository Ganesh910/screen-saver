import numpy as np
import matplotlib.pyplot as plt
from attractors import Attractors as at
# from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Define the Lorenz attractor function
# def lorenz(x, y, z, s=10, r=28, b=8//3):
#     x_dot = s*(y - x)
#     y_dot = r*x - y - x*z
#     z_dot = x*y - b*z
#     return x_dot, y_dot, z_dot

# Set up the figure and axes for the 3D plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim((-20, 20))
ax.set_ylim((-20, 20))
ax.set_zlim((0, 50))
ax.axis('off')
ax.grid(False)
ax.set_facecolor('none')

# Set up the initial conditions and time step
dt = 0.01
T = 100
N = int(T/dt)
xs = np.empty(N + 1)
ys = np.empty(N + 1)
zs = np.empty(N + 1)
xs[0], ys[0], zs[0] = (1, 1, 1)

# Generate the Lorenz attractor data
for i in range(N):
    x_dot, y_dot, z_dot = at.newton_leipnik(xs[i], ys[i], zs[i])
    xs[i+1] = xs[i] + (x_dot * dt)
    ys[i+1] = ys[i] + (y_dot * dt)
    zs[i+1] = zs[i] + (z_dot * dt)

# Define the update function for the animation
def update(num, data, line):
    line.set_data(data[:2, :num])
    line.set_3d_properties(data[2, :num])
    return line,

# Set up the animation
data = np.array([xs, ys, zs])
line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])
ani = FuncAnimation(fig, update, frames=N, fargs=(data, line), interval=0.5, blit=True)

# Show the animation
plt.rcParams['toolbar'] = 'None'
plt.show()