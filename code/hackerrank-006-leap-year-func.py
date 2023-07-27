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