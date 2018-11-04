infile = open("NYTimes.txt",'r')
timesList = [line.rstrip() for line in infile]
infile.close()
timesSet = set(timesList)

infile = open("WSJ.txt",'r')
wsjList = [line.rstrip() for line in infile]
infile.close()
wsjSet = set(wsjList)

combinationSet = timesSet.union(wsjSet)
combinationList = list(combinationSet)
combinationString = ('\n').join(combinationList)

outfile = open("NewFile.txt",'w')
outfile.write(combinationString)
outfile.close()



