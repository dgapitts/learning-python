import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x = np.linspace(-1, 5, 100)

x0 = 2
slope = 2 * x0

tangent = f(x0) + slope * (x - x0)

plt.plot(x, f(x), label="f(x) = x²")
plt.plot(x, tangent, label="tangent at x = 2")
plt.scatter([x0], [f(x0)])

plt.legend()
plt.grid()
plt.show()
