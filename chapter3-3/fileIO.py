infile = open("d:\\data\\input.txt",'r')
list = []
for line in infile:
    var = eval(line.strip())
    if var >0:
        list.append(var)

avg = sum(list)/len(list)
vSum = 0
for i in range(len(list)):
    vSum += (list[i]-avg)**2
variance = vSum / len(list)

for i in range(len(list)):
    print(list[i],end=" ")
    if (i+1) %10 == 0:
        print()
print()
print()
print("min: {}".format(min(list)))
print("max: {}".format(max(list)))
print("avg: {0:.2f}".format(avg))
print("variance : {0:.2f}".format(variance))