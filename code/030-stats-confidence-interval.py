'''
If our sampled proportion is, p, its complement is q=1−p, 
and the number of individuals in the sample is  n, 
then the standard error is given by:

SE = sqrt((pq/n)) 

For example, according to a survey conducted in December 
2017 by Bertelsmann Stiftung, the 
45
th
  U.S. president— Donald Trump— was very unpopular in the European Union. Among 
36,000 respondents from all over Europe, only 
23% approved of President Trump.

'''
import math
n=36000
#p=270
proportion=0.23
print (round(math.sqrt(proportion*(1-proportion)/n),3))
