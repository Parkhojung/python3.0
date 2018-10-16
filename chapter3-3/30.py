degree = 212
minute = 0
while degree > 150:
    degree -= 0.079*(degree - 70)
    minute +=1

print("The coffee will cool to below 150 degrees in {} minutes.".format(minute))