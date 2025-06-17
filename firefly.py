import numpy as np
import matplotlib
matplotlib.use("TkAgg")  # Ensure compatibility when running as .py
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create spiral path
theta = np.linspace(0, 8 * np.pi, 500)
radius = np.exp(0.02 * theta)
x_data = radius * np.cos(theta)
y_data = radius * np.sin(theta)

# Set up figure
fig = plt.figure(figsize=(6, 6), facecolor="black")
ax = fig.add_subplot(1, 1, 1, facecolor="black")  # Ensure both fig and ax are dark

ax.axis("off")
ax.set_xlim(-120, 120)
ax.set_ylim(-120, 120)

# Firefly and trail
firefly, = ax.plot([], [], 'o', color='gold', markersize=10)
trail, = ax.plot([], [], color='lightyellow', linewidth=0.8, alpha=0.5)

def init():
    firefly.set_data([], [])
    trail.set_data([], [])
    return firefly, trail

def animate(i):
    if i < len(x_data):
        firefly.set_data([x_data[i]], [y_data[i]])
        trail.set_data(x_data[:i], y_data[:i])
        firefly.set_alpha(0.5 + 0.4 * np.sin(i / 10))
    return firefly, trail

ani = FuncAnimation(
    fig, animate, init_func=init, frames=len(x_data),
    interval=30, blit=True, repeat=False
)

ani.save("firefly_spiral.gif", writer="pillow", fps=30) #in case you want to save

plt.show()
