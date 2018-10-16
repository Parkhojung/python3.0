restMoney = float(input("Enter amount of deposit: "))
year =0
while restMoney > 600:
    restMoney = 1.003*restMoney - 600
    year +=1
print("Balance will be ${0:.2f} after {1:} months.".format(restMoney,year))