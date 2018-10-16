def getN(n):
    res =1
    for i in range(n,0,-1):
        res*=i
    return res

num =int(input("Enter a positive integer: "))
res = getN(num)
print("{}! is {}".format(num,res))