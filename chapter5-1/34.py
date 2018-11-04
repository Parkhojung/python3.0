infile = open("Numbers.txt",'r')
numList = [line for line in infile]
print("The file Numbers.txt contains {} numbers.".format(len(numList)))