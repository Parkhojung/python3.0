month = int(input("Enter number of months: "))
year = month // 12
month2 = month % 12
print("{0:d} months is {1:d} years and {2:d} months.".format(month,year,month2))