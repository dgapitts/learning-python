import math
def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, round(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True
    
def primeCount(n):
    # Write your code here
    count = 0
    mult = 1
    for i in range(2, math.ceil(math.sqrt(n))+1):
        if is_prime(i):
            mult *= i
            if mult <= n:
                count += 1
            else:
                break

    return count

# Example usage:
print(primeCount(6))  
print(primeCount(1)) 
print(primeCount(2)) 
print(primeCount(3)) 
print(primeCount(50)) 
print(primeCount(500)) 

"""
sample output:

~/projects/learning-python/code main $ python3 math-hackerrank-001-primeCount.py
0
1
3
6

"""