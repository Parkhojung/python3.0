def main():
    numbers = [865,1169,1208,1243,290]
    list1 = [str(i) for i in numbers]

    numbers.sort(key= fun)

    print("Sorted by sum of digits: ")
    print(numbers)

def fun(num):
    sum = 0
    p = 1
    for di in reversed(str(num)):
        sum += int(di)

    return sum
main()