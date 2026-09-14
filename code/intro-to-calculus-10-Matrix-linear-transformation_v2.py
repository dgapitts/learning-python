import sympy as sp

x, y = sp.symbols('x y')

A = sp.Matrix([
    [2, 0],
    [0, 1]
])

v = sp.Matrix([x, y])

print("A:")
sp.pprint(A)

print("\nv:")
sp.pprint(v)

print("\nA @ v:")
sp.pprint(A * v)
