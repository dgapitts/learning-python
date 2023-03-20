# 002_collatz_challenge

Consider the following sequence:
```
Choose a positive integer
If the number is even divide it by 2
if it is odd multiply by 3 and 1
Repeat step 
```
> The Collatz conjecture asserts that following these steps will always lead to 1, for any starting integer greater than 

and demoing this process - starting with 5 ...

```
(base) ~/projects/brilliant-Programming-with-Python $ cat code/002_collatz_challenge.py
number = 5
steps = 0

for i in range(200):
    if number == 1:
        break
    if number%2 == 0:
        number=number/2
        steps=steps+1
    else:
        number=number*3+1
        steps=steps+1

if number == 1:
    print("It took", steps, "steps")
else:
    print("The number didn't reach 1 yet")
(base) ~/projects/brilliant-Programming-with-Python $ python code/002_collatz_challenge.py
It took 5 steps
(base) ~/projects/brilliant-Programming-with-Python $ ## 5 > 16 > 8 > 4 > 2 > 1
(base) ~/projects/brilliant-Programming-with-Python $
````


