import numpy as np

def f(x):
    return x**3 - 3*x

def derivative(f, x, h=0.0001):
    return (f(x + h) - f(x)) / h

x_values = np.linspace(-3, 3, 10000)

for x in x_values:
    if abs(derivative(f, x)) < 0.001:
        print(f"x ≈ {x:.4f}, f(x) ≈ {f(x):.4f}")
