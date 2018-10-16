str = input("Enter number: ")
index = str.index('.')
lStr = str[:index]
rStr = str[index+1:]
lLen = lStr.__len__()
rLen = rStr.__len__()
print("{0:d} digits to left of decimal point".format(lLen))
print("{0:d} digits to right of decimal point".format(rLen))