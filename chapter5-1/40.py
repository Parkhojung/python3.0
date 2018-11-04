infile = open("SomeMonths.txt")
mList = [line.rstrip() for line in infile if 'r' not in line]
infile.close()

outfile = open("SomeMonths.txt",'w')
for month in mList:
    outfile.write(month+'\n')

