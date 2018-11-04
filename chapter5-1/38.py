infile = open("Numbers.txt",'r')
numList = [eval(line) for line in infile]
print("The average of the numbers in the file Numbers.txt is {}".format(sum(numList)/len(numList)))