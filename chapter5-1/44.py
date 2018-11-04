infile =open("PresStates.txt",'r')
stateSet = set([line.rstrip() for line in infile])
infile.close()
print("{} different states have produced presidents "
      "of the United States.".format(stateSet.__len__()))
