import numpy as np
import matplotlib.pyplot as plt

def regula_falsi(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Szelő módszer (Regula Falsi) a f(x) függvény gyökének közelítésére.
    
    Paraméterek:
    f       - A vizsgált függvény
    x0, x1  - Kezdőértékek (f(x0) és f(x1) ellentétes előjelű)
    tol     - Hibaküszöb
    max_iter - Iterációk maximális száma
    
    Visszatérési érték:
    A közelített gyök vagy None, ha nem konvergál.
    """
    iter_points = [(x0, f(x0)), (x1, f(x1))]
    
    for _ in range(max_iter):
        if abs(f(x1) - f(x0)) < 1e-12:  # Nullával osztás elkerülése
            print("A módszer nem működik: osztás nullával.")
            return None, iter_points
        
        x_next = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        iter_points.append((x_next, f(x_next)))
        
        if abs(f(x_next)) < tol:
            return x_next, iter_points
        
        if f(x0) * f(x_next) < 0:
            x1 = x_next
        else:
            x0 = x_next
    
    print("A módszer nem konvergált a maximális iterációszám alatt.")
    return None, iter_points

# Tesztelés egy példafüggvénnyel
def f(x):
    return x**3 - x - 2  # Egy nemlineáris egyenlet

root, iter_points = regula_falsi(f, 2, 1.2)
print("Talált gyök:", root)

# Grafikon rajzolása
x_vals = np.linspace(0, 2, 100)
y_vals = f(x_vals)

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label="f(x) = x^3 - x - 2", color="blue")
plt.axhline(0, color="black", linewidth=1)
plt.axvline(root, color="red", linestyle="--", label=f"Gyök: {root:.6f}")

# Iterációs pontok ábrázolása
iter_x, iter_y = zip(*iter_points)
plt.scatter(iter_x, iter_y, color="green", zorder=3, label="Iterációs pontok")
plt.plot(iter_x, iter_y, color="green", linestyle="dashed", alpha=0.6)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Szelő módszer alkalmazása")
plt.legend()
plt.grid()
plt.show()
