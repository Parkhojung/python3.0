salary = float(input("Enter beginning salary: "))
newSal = salary*1.05**3
print("New salary: ${0:,.2f}".format(newSal))
change = (newSal-salary)/salary
print("Change: {0:.2%}".format(change))