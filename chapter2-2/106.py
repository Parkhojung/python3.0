amt = float(input("Enter amount of bill: "))
per = float(input("Enter percentage tip: "))
tip = amt*per/100
print("Tip: ${0:.2f}".format(tip))