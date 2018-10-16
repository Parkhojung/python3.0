N = int(input("Enter a positive integer(>1): "))
F = 2
while N >1:
    if (N%F) == 0:
        print(F, end=" ")
        N = N/F
    else:
        F +=1

