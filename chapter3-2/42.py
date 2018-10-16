list =[]
cost1= float(input("Enter cost of first suit: "))
cost2 = float(input("Enter cost of second suit: "))
list.append(cost1)
list.append(cost2)
totalCost =0
if list[0] > list[1]:
    totalCost = list[0]+list[1]*0.5
else :
    totalCost = list[0]*0.5 + list[1]

print("Cost of the two suits is ${0:.2f}".format(totalCost))