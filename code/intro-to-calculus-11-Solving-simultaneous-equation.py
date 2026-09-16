import numpy as np

A = np.array([
    [2, 1],
    [1, -1]
])

b = np.array([5, 1])

print("A:")
print(A)

print("\nb:")
print(b)

print("\nnp.linalg.solve(A, b):")
print(np.linalg.solve(A, b))

#solution = np.linalg.solve(A, b)

# print(solution)


