import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def g(x):
    return - (x**2) / 4 - x / 2 + 4  # Új függvény

def fixed_point_iteration(g, x0, iterations=9):
    x_values = [x0]
    for _ in range(iterations):
        x_next = g(x_values[-1])
        x_values.append(x_next)
    return x_values

def animate_fixed_point(g, x_values):
    fig, ax = plt.subplots()
    x = np.linspace(-1, 3, 400)
    y = g(x)
    
    ax.plot(x, y, label='$g(x) = -\\dfrac{x^2}{4} - \\dfrac{x}{2} + 4$', color='blue')

    ax.plot(x, x, '--', label='$y=x$', color='gray')
    
    point, = ax.plot([], [], 'ro', markersize=5)
    lines_v = []  # Függőleges vonalak listája
    lines_h = []  # Vízszintes vonalak listája
    for _ in range(len(x_values) - 1):
        line_v, = ax.plot([], [], 'k-', alpha=0.6)
        line_h, = ax.plot([], [], 'k-', alpha=0.6)
        lines_v.append(line_v)
        lines_h.append(line_h)
    
    def update(i):
        if i == 0:
            return point, *lines_v, *lines_h
        x_prev, x_curr = x_values[i-1], x_values[i]
        y_curr = g(x_prev)
        lines_v[i-1].set_data([x_prev, x_prev], [x_prev, y_curr])
        lines_h[i-1].set_data([x_prev, x_curr], [y_curr, y_curr])
        point.set_data([x_curr], [x_curr])
        return point, *lines_v, *lines_h
    
    ani = animation.FuncAnimation(fig, update, frames=len(x_values), interval=400, repeat=False)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$g(x)$')
    ax.legend()
    ax.set_title('Fixpontos iteráció animáció')
    plt.show()

# Kezdőérték
x0 = 1.97
x_values = fixed_point_iteration(g, x0)
animate_fixed_point(g, x_values)
