def f(x):
    return x**2

def derivative(f, x, h=0.001):
    return (f(x + h) - f(x)) / h

for h in [1, 0.1, 0.01, 0.001, 0.0001]:
    print(h, derivative(f, 3, h))
