num = int(input("Enter number of bagels: "))
centCost =0
if num< 6:
    centCost = num*75
else:
    centCost = num*60

dollarCost = centCost/100
print("Cost is ${0:.2f}.".format(dollarCost))