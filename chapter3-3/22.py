cpi  = 238.25
goal = cpi*2
year =0
while cpi < goal:
    cpi *= 1.025
    year +=1

print("Consumer prices will double in {0:d} years.".format(year))
