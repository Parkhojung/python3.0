months=[]
def fileRead(infile):
    for line in infile:
        months.append(line.rstrip())
def delNotHaveR():
    i = 0
    res = True
    while res == True:
        if 'r' not in months[i]:
            del months[i]
        else:
            i+=1
        if i == len(months):
            res = False
def printList():
    print("The R months are:")
    for item in months:
        if item == months[-1]:
            print(item,end="")
            break
        print(item,end=", ")
def main():
    infile = open("d:\\data\\input.txt",'r')
    for line in infile:
        months.append(line.rstrip())
    fileRead(infile)
    delNotHaveR()
    printList()
main()