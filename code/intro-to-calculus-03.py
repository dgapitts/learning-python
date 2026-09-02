def f(x):
    return x**2

def derivative(f, x, h=0.001):
    return (f(x + h) - f(x)) / h

print(f"{'h':>10}  {'derivative':>12}")
print("-" * 24)

for h in [1, 0.1, 0.01, 0.001, 0.0001]:
    result = derivative(f, 3, h)
    print(f"{h:10g}  {result:12.6f}")

