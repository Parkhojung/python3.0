totalD = 0
month = 0
while totalD < 3000:
    totalD = 1.0025*totalD+100
    month += 1

print("Annuity will be worth more than $3000 after {0:d} months.".format(month))