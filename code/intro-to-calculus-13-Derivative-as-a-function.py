import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

def derivative(f, x, h=0.0001):
    return (f(x + h) - f(x)) / h

x = np.linspace(-5, 5, 200)

y = f(x)
dy = derivative(f, x)

plt.plot(x, y, label="f(x) = x²")
plt.plot(x, dy, label="f'(x) ≈ 2x")

plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.legend()
plt.show()



