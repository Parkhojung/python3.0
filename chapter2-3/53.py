amount = float(input("Enter amount of bill: "))
percent = float(input("Enter percentage tip: "))/100
tip = amount * percent
print("Tip: ${0:.2f}".format(tip))
