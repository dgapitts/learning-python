'''
If our sampled proportion is, p, its complement is q=1−p, 
and the number of individuals in the sample is  n, 
then the standard error is given by:

SE = sqrt((pq/n)) 

After examining 

900 trees in our local forest, we find that 
280 of them are maple trees.
'''
import math
n=900
p=270
proportion=p/n
print (round(math.sqrt(proportion*(1-proportion)/n)*100,2))