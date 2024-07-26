def handshakes(people):
   n = int(people)
   return n * (n - 1) // 2


print(handshakes(1))
print(handshakes(2))
print(handshakes(3))
print(handshakes(4))

"""
sample output:

~/projects/learning-python/code main $ python3 math-hackerrank-001-handshakes.py
0
1
3
6

"""