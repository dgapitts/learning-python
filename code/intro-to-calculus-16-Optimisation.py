import numpy as np
import matplotlib.pyplot as plt

def area(x):
    return x * (10 - x)

def derivative(f, x, h=0.0001):
    return (f(x + h) - f(x)) / h

x = np.linspace(0, 10, 500)

areas = area(x)
dareas = derivative(area, x)

plt.plot(x, areas, label="Area")
plt.plot(x, dareas, label="Derivative")
plt.axhline(0)
plt.grid()
plt.legend()
plt.show()
