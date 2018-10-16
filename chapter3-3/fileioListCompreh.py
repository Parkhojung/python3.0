infile = open("d:\\data\\input.txt",'r')
list = []
n = 0
list = [eval(line.rstrip()) for line in infile if eval(line.rstrip()) >0]
for i in range(len(list)): #파일 입력 확인
    print(list[i],end=" ")
    if (i+1) %10 == 0:
        print()

avg = sum(list)/len(list) #평균 계산
vSum = 0
for i in range(len(list)): #분산 계산
    vSum += (list[i]-avg)**2
variance = vSum / len(list)
print("\n\nmin: {}".format(min(list)))
print("max: {}".format(max(list)))
print("avg: {0:.2f}".format(avg))
print("variance : {0:.2f}".format(variance))