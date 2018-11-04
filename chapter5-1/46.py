nameSet = set()
infile =open("Names.txt",'r')
nameSet = {line.rstrip() for line in infile}
infile.close()

str= input("이름을 입력하세요: ")
nameSet.add(str)
nameList = list(nameSet)
nameList.sort()


outfile = open("Names.txt",'w')
for name in nameList:
    outfile.write(name+'\n')
outfile.close()