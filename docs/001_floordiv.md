### 001 floordiv operator //

I am very familiar with the modular (%) operator, but didn't know the double-slash (//) was a round down operator #TIL e.g. 130 secs is 2 mins and 10 secs
```
>>> print(130//60)
2
>>> print(130%60)
10
``` 

i.e. as per doco

```
operator.floordiv(a, b)¶
operator.__floordiv__(a, b)
Return a // b.
```

https://docs.python.org/3/library/operator.html
