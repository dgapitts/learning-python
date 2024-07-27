import math

def gameWithCells(n, m):
    horizontal_drops = math.ceil(n / 2)
    vertical_drops = math.ceil(m / 2)
    return horizontal_drops * vertical_drops



print(gameWithCells(2,2))
print(gameWithCells(4,6))
print(gameWithCells(5,3))
"""
sample output:

~/projects/learning-python/code main $ python3 math-hackerrank-003-gameWithCells.py
1
6
6

"""