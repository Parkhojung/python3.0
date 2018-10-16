wage = float(input("Enter hourly wage: "))
hour = float(input("Enter number of hours worked: "))

pay =0
if hour >40:
    pay = (40*wage)+(1.5*wage*(hour-40))
else :
    pay = hour*wage

print("Gross pay for week is ${0:.2f}.".format(pay));
