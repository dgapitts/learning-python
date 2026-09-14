import numpy as np

A = np.array([
    [2, 0],
    [0, 1]
])

x = 3
y = 4

v = np.array([x, y])

print("A:")
print(A)

print("\nv:")
print(v)

print("\nA @ v:")
print(A @ v)
