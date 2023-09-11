'''

This is a helper script for the mathematical methods developed by the ancient Egyptians
https://en.wikipedia.org/wiki/Ahmes.

For example using doubling, we can break down 24 * 21 

~/projects/brilliant-Programming-with-Python/code $ python3 010-ancient-maths-ahmes.py 
1:21
2:42
4:84
8:168
16:336

to the easier 168 + 336 = 504

'''

for i in [1,2,4,8,16]:
    print (str(i)+":"+str(i*21))

