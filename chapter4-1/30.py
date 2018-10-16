def inputFun():
    fName=input("Enter first name:")
    lName=input("Enter last name: ")
    sal = int(input("Enter current salary: "))
    return fName,lName,sal

def calc(sal):
    res = 0
    if sal <40000:
        res = sal*1.05
    else :
        res = 42000+ (sal-40000)*1.02
    return res

fName,lName,sal = inputFun()
res = calc(sal)
print("New salary for {0:} {1:}: ${2:,.2f}".format(fName,lName,res))