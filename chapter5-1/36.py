infile = open("Numbers.txt",'r')
numList = [line for line in infile]
print("The smallest number in the file Numbers.txt is {}".format(min(numList)))