tBarcket = float(input("Enter tax bracket(as decimal): "))
bRate = float(input("Enter municipal bond interest rate(as %): " ))
cRate = bRate/((1-tBarcket)*100)
print("Equivalent CD interest rate: {0:.3%}".format(cRate))