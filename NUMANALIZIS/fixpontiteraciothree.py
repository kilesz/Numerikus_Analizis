import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def g(x):
    return (x**2) / 4 + x / 2  # Módosított függvény az x = x^2/4 + x/2 egyenlethez

def fixed_point_iteration(g, x0, iterations=15):
    x_values = [x0]
    for _ in range(iterations):
        x_next = g(x_values[-1])
        x_values.append(x_next)
    return x_values

def animate_fixed_point(g, x_values):
    fig, ax = plt.subplots()
    x = np.linspace(-0.5, 3, 400)
    y = g(x)
    
    ax.plot(x, y, label='$g(x) = \frac{x^2}{4} + \frac{x}{2}$', color='blue')
    ax.plot(x, x, '--', label='$y=x$', color='gray')
    
    point, = ax.plot([], [], 'ro', markersize=5)
    lines_v = []  # Függőleges vonalak listája
    lines_h = []  # Vízszintes vonalak listája
    for _ in range(len(x_values) - 1):
        line_v, = ax.plot([], [], 'k-', alpha=0.6)  # Függőleges vonal
        line_h, = ax.plot([], [], 'k-', alpha=0.6)  # Vízszintes vonalak
        lines_v.append(line_v)
        lines_h.append(line_h)
    
    def update(i):
        if i == 0:
            return point, *lines_v, *lines_h
        x_prev, x_curr = x_values[i-1], x_values[i]
        y_curr = g(x_prev)
        lines_v[i-1].set_data([x_prev, x_prev], [y_curr, x_prev])  # Függőleges vonal módosítása
        lines_h[i-1].set_data([x_curr, x_prev], [y_curr, y_curr])  # Vízszintes lépés balra
        point.set_data([x_curr], [x_curr])  # Mozgó pont az iteráción
        return point, *lines_v, *lines_h
    
    ani = animation.FuncAnimation(fig, update, frames=len(x_values), interval=400, repeat=False, blit=True)  # Blit optimalizáció
    plt.show()
    return ani  # Objektumot vissza kell adni, hogy ne törlődjön

# Kezdőérték
x0 = 2.03  
x_values = fixed_point_iteration(g, x0)
ani = animate_fixed_point(g, x_values)
