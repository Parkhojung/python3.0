def main():
    name1,name2,sal = inputNum()
    sal = cal(sal)
    prn(name1,name2,sal)

def inputNum():
    name1 = input("Enter first name: ")
    name2 = input("Enter last name: ")
    sal = int(input("Enter current salary: "))
    return name1,name2,sal

def cal(sal):
    if sal < 40000:
        sal = sal*1.05
    else:
        sal = sal + 2000+ (sal-40000)*0.02
    return sal
def prn(name1,name2,sal):
    print("New salary for {0:s} {1:s}: ${2:,.2f}.".format(name1,name2,sal))

main()