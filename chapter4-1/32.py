months=[]

def fileRead(infile):
    for line in infile:
        months.append(line.rstrip())

def delNotHaveR():
    i = 0
    res = True
    while res == True:
        print(i,months)
        if 'r' not in months[i]:
            del months[i]
        else:
            i+=1

        if i == len(months):
            res = False

def printList():
    print("The R months are:")
    for item in months:
        print(item,end=", ")

def main():
    infile = open("d:\\data\\input.txt",'r')
    for line in infile:
        months.append(line.rstrip())
 #   print(months)
    fileRead(infile)
 #   print(months)
    delNotHaveR()
    print(months)
#    printList()

main()