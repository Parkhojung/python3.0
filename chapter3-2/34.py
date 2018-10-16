balance = float(input("Enter current balance: "))
withdrawal = float(input("Enter amount of withdrawal: "))

newBalance = balance - withdrawal

if newBalance < 0 :
    print("Withdrawl denied.")
elif newBalance <150:
    print("Balance below $150")
else :
    print("The new balance is ${0:.2f}.".format(newBalance))