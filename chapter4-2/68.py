def main():
    rate,pay,beg = inputNum()
    res1,res2,res3 = cal(rate,pay,beg)
    prn(res1,res2,res3)

def inputNum():
    num1 = float(input("Enter annual rate of interest: "))
    num1 = num1/100
    num2 = float(input("Enter monthly payment: "))
    num3 = float(input("Enter beg. of month balance: "))
    return num1,num2,num3

def cal(rate,pay,beg):
    rate = rate/12

    interest = beg*rate
    temp = beg
    beg = beg*(1+rate) - pay
    reduce = temp-beg

    return interest,reduce ,beg

def prn(res1,res2,res3):
    print("Interest paid for the month: ${0:.2f}".format(res1))
    print("Reduction of principal: ${0:.2f}".format(res2))
    print("End of month balance: ${0:,.2f}".format(res3))

main()