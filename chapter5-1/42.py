

def vowelCheck(line):
    if line[0].lower() in ['a','e','i','o','u']:
        return 1
    else:
        return -1

infile = open("SomeStates.txt",'r')
list1 = [line for line in infile if vowelCheck(line)==1 ]
infile.close()
outfile = open("SomeStates.txt",'w')
for line in list1:
    outfile.write(line)