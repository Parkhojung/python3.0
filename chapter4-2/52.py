def main():
    list1 = inputNum5()
    range,avg = cal(list1)
    print("Range:",str(range))
    print("Average:",str(round(avg)))
def inputNum5():
    num1 = int(input("Enter grade 1: "))
    num2 = int(input("Eeter grade 2: "))
    num3 = int(input("Enter grade 3: "))
    num4 = int(input("Eeter grade 4: "))
    num5 = int(input("Enter grade 5: "))
    list = [num1,num2,num3,num4,num5]
    return list
def cal(list1):
    list1.sort()
    list2 = [i for i in list1[2:]]
    range  = max(list2)- min(list2)
    avg = sum(list2)/len(list2)
    return range,avg
main()