import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 3*x

def derivative(f, x, h=0.001):
    return (f(x + h) - f(x)) / h

def second_derivative(f, x, h=0.001):
    return (
        f(x + h)
        - 2*f(x)
        + f(x - h)
    ) / h**2

x = np.linspace(-3, 3, 400)

plt.plot(x, f(x), label="f(x)")
plt.plot(x, derivative(f, x), label="f'(x)")
plt.plot(x, second_derivative(f, x), label="f''(x)")

plt.axhline(0)
plt.grid()
plt.legend()
plt.show()
