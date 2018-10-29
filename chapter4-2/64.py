#미완성

file = open("States.txt","r")
list1 = [line.rstrip() for line in file]
list1.sort(reverse=True)
print(list1[:])