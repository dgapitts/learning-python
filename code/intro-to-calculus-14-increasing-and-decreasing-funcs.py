# intro-to-calculus-14.py

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 3*x

def derivative(f, x, h=0.0001):
    return (f(x + h) - f(x)) / h

x = np.linspace(-3, 3, 400)

y = f(x)
dy = derivative(f, x)

plt.plot(x, y, label="f(x)")
plt.plot(x, dy, label="f'(x)")
plt.axhline(0)
plt.grid()
plt.legend()
plt.show()
