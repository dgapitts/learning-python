'''
If our sampled proportion is, p, its complement is q=1−p, 
and the number of individuals in the sample is  n, 
then the standard error is given by:

SE = sqrt((pq/n)) 

According to the Institute for Health Metrics and Evaluation, during the years 

2010−2016 (a period that saw an Ebola outbreak in Western Africa), the odds of a fifteen-year-old woman dying from Ebola in Sierra Leone was 13.5%.
13.5%. 

This data was based on the survey of 519 individuals.

'''
import math
n=519
#p=270
proportion=0.135
print (round(math.sqrt(proportion*(1-proportion)/n)*100,2))