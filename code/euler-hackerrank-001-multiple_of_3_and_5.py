
import time
def multiple_of_3_and_5(n):
    multiples=[]
    for i in range(1,n):
        if i%3==0 or i%5==0:
        	#print(i)
        	multiples.append(i)
    return multiples


#starttime = time.clock()
print (sum(multiple_of_3_and_5(100)))
print (sum(multiple_of_3_and_5(0)))
print (sum(multiple_of_3_and_5(10000000)))
print (sum(multiple_of_3_and_5(100000000)))
#print (time.clock()-starttime)

