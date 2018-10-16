cycleT = eval(input("Enter number of hours cycling: "))
runT = eval((input("Enter number of hours running: ")))
swimT = eval((input("Enter number of hours swimming: ")))
use = 200*cycleT + 475*runT + 275*swimT
loss = use/3500
print("Weight loss: {0:.1f} pounds".format(loss))