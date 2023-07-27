def is_leap(year):
    leap = False

    # most years are clearly not leap years
    if (year%4)== 0:
       leap = True
    else:
       return leap

    # edges for every 100 years (excluding every 400th year)
    if (year%100)== 0:
       leap = False
    if (year%400)== 0:
       leap = True

    return leap
˝

print(is_leap(1500))
print(is_leap(1600))
print(is_leap(1700))
print(is_leap(1800))
print(is_leap(1900))
print(is_leap(2000))
print(is_leap(2001))
print(is_leap(2002))
print(is_leap(2003))
print(is_leap(2004))
print(is_leap(2005))
print(is_leap(2006))
print(is_leap(2007))