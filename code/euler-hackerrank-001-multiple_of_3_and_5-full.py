#!/bin/python3

import sys
import logging
t = int(input().strip())
def multiple_of_3_and_5(n):
    multiples=[]
    for i in range(1,n):
        if i%3==0 or i%5==0:
            #print(i)
            multiples.append(i)
    return multiples


#starttime = time.clock()

    

for a0 in range(t):
    n = int(input().strip())
    #logging.info(n)
    print (str(sum(multiple_of_3_and_5(n))))

