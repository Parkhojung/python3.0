salary = float(input("Enter beginning salary: "))
upSal = salary*1.1
downSal = upSal*0.9
change = (downSal-salary)/salary
print("New salary: ${0:,.2f}".format(downSal))
print("Change: {0:.2%}".format(change))