def max_prime_factor(num):
    while num % 2 == 0:
        max_factor = 2
        num //= 2

    for factor in range(3, int(num**0.5) + 1, 2):
        while num % factor == 0:
            max_factor = factor
            num //= factor

    if num > 2:
        max_factor = num

    return max_factor

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(max_prime_factor(n))
