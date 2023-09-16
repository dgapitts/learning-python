import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    # Using the sum of an arithmetic progression sum = x/2 * (2 * a + (x - 1) * d)
    # x = the number of terms to be added
    # a = the first term in the sequence
    # d = the constant value between terms

    # How many multiples of 3 under n? i.e. number of terms to be added.
    multiples_of_3 = (n - 1) // 3
    # How many multiples of 5 under n? i.e. number of terms to be added.
    multiples_of_5 = (n - 1) // 5
    # How many multiples of 15 under n? i.e. number of terms to be added.
    multiples_of_15 = (n - 1) // 15
    
    # Arithmetic sum of multiples of 3
    sum_multiples_of_3 = multiples_of_3/2 * (2 * 3 + (multiples_of_3 - 1) * 3)
    # Arithmetic sum of multiples of 5
    sum_multiples_of_5 = multiples_of_5/2 * (2 * 5 + (multiples_of_5 - 1) * 5)
    # Arithmetic sum of multiples of 15
    sum_multiples_of_15 = multiples_of_15/2 * (2 * 15 + (multiples_of_15 - 1) * 15)
    # Add the sum of the multiples of 3 and 5 and remove the multiples of 15
    print(int(sum_multiples_of_3 + sum_multiples_of_5 - sum_multiples_of_15))<
