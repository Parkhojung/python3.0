num = int(input("Enter number of copies: "))
centCost = 0
if num <=100:
    centCost = num*5
else:
    centCost = 100*5 + (num-100)*3

dollarCost = centCost/100
print("Cost is ${0:.2f}.".format(dollarCost))