def f(x):
    return x**2

def derivative(f, x, h=0.001):
    return (f(x + h) - f(x)) / h

print(derivative(f, 3))
