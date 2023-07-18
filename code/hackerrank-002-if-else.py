import re
import sys

'''
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5 , print Not Weird
If  is even and in the inclusive range of 6 to 20 , print Weird
If  is even and greater than , print Not Weird
'''


if __name__ == '__main__':
    n = int(input().strip())
    if n%2 == 1:
       print ("Weird")
    else:
       if n >= 6 and n<=20:
          print ("Weird")
       else:
          print ("Not Weird")