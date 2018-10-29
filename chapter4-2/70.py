def main():
    num = int(input("Enter an integer greater than 1: "))
    res = isPrime(num)
    if res:
        print("{0:d} is a prime number.".format(num))
    else:
        print("{0:d} is not a prime number".format(num))
def factorial(n):
    res = 1
    for i in range(n,0,-1):
        res *=i
    return res
def isPrime(n):
    checkNum = factorial(n-1)+1
    if checkNum%n == 0 :
        return True
    else:
        return False

main()