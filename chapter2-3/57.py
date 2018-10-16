principal = float(input("Enter principal: "))
rate = float(input("Enter interest rate (as %): "))
year = int(input("Enter number of years: "))
value = principal*(1+rate/100)**year
print("Future value: ${0:,.2f}".format(value))