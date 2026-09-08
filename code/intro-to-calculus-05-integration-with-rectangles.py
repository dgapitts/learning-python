def f(x):
    return x**2

a = 0
b = 2
n = 1000

dx = (b - a) / n

area = 0

for i in range(n):
    x = a + i * dx
    area += f(x) * dx

print(area)
