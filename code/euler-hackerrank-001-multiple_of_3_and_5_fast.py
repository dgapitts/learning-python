
import time
def sum_multiple_of_3_and_5(n):
    multiples_of_3 = (n - 1) // 3
    multiples_of_5 = (n - 1) // 5
    multiples_of_15 = (n - 1) // 15
    sum_multiples_of_3 = multiples_of_3/2 * (2 * 3 + (multiples_of_3 - 1) * 3)
    sum_multiples_of_5 = multiples_of_5/2 * (2 * 5 + (multiples_of_5 - 1) * 5)
    sum_multiples_of_15 = multiples_of_15/2 * (2 * 15 + (multiples_of_15 - 1) * 15)
    return (round(sum_multiples_of_3 + sum_multiples_of_5 - sum_multiples_of_15))


print (sum_multiple_of_3_and_5(100))
print (sum_multiple_of_3_and_5(0))
print (sum_multiple_of_3_and_5(10000000))
print (sum_multiple_of_3_and_5(100000000))
#print (time.clock()-starttime)

