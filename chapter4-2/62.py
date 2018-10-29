file = open("USPres.txt")
list = [infile.rstrip() for infile in file]

list.sort(key=lambda x : x.split()[-1])
for i in list[:6]:
    print(i)