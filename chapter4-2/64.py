#미완성

file = open("States.txt","r")
list1 = [line.rstrip() for line in file]
list1.sort(key =len,reverse=True)
for item in list1[:6]:
    print(item)