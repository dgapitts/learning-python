#!/bin/python3

import sys


def largest_prime_factors(n):
    factors=[]
    d=1
    while n>1:
        d=d+1
        if n%d==0:
            n=n/d
            factors.append(d)
    return factors[-1]

    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(largest_prime_factors(n))
<
