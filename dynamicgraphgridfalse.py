import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = []
y = []

fig, ax = plt.subplots()

def update(frame):
    x.append(frame)
    y.append(frame*5)

    ax.clear()
    ax.plot(x, y, marker='o')
    ax.set_xlabel("X values")
    ax.set_ylabel("Y values")
    ax.set_title("Dynamic Graph - Grid False")
    ax.grid(False)

ani = FuncAnimation(fig, update, frames=range(1,10), interval=1000)

plt.show()