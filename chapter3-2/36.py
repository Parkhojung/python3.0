year = int(input("Enter a year: "))

if year%4 ==0:
    if year % 400 ==0:
        print("{0:d} is a leap year.".format(year))
    elif year % 100 ==0:
        print("{0:d} is not a leap year.".format(year))
    else:
        print("{0:d} is a leap year.".format(year))
else:
    print("{0:d} is not a leap year.".format(year))