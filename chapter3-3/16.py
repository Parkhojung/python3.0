coef = float(input("Enter coefficient of restitution: "))
height = float(input("Enter initial height in meters: "))
cnt =0
travel = 0
while True:
    if height > .1:
        cnt +=1
    travel += height
    height *= coef
    if(height <.1):
        break
    travel += height


print("Number of bounces: {0:d}".format(cnt))
print("Meters traveled: {0:.2f}".format(travel))
