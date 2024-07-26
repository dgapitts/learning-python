def lowestTriangle(base, area):
    height = (2 * area) / base
    return int(height) if height == int(height) else int(height) + 1


print(lowestTriangle(4,6))
print(lowestTriangle(2,2))
print(lowestTriangle(17,100))
"""
sample output:

~/projects/learning-python/code main $ python3 math-hackerrank-001-lowestTriangle.py
0
1
3
6

"""