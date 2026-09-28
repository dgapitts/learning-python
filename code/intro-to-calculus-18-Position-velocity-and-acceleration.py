# intro-to-calculus-18.py

import numpy as np
import matplotlib.pyplot as plt

def position(t):
    return t**3 - 6*t**2 + 9*t

def derivative(f, x, h=0.0001):
    return (f(x + h) - f(x)) / h

def velocity(t):
    return derivative(position, t)

def acceleration(t):
    return derivative(velocity, t)

t = np.linspace(0, 5, 500)

plt.plot(t, position(t), label="position")
plt.plot(t, velocity(t), label="velocity")
plt.plot(t, acceleration(t), label="acceleration")

plt.axhline(0)
plt.xlabel("time")
plt.grid()
plt.legend()
plt.show()
