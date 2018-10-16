revenue = float(input("Enter revenue: "))
expense = float(input("Enter expenses: "))
income = revenue - expense
print("Net income: ${0:,.2f}".format(income))