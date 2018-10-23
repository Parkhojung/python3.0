

# list = ['r', 'ar', 'br', 'a', 'b']
#
# for a in reversed(list):
#     str = a
#     print(str)
#     if 'r' in str:
#         list.remove(str)
#
# print(list)
#
#
# num = 0.5
# print("{:,.2%}".format(num))
#
# list1 = [1,2,3]
# list2= ((4,5,6),[7,8,9])
# list1.extend(list2)
# del list1[1:3]
# print(list1)
#
# str = "a  b     c d"
# list3 = str.split()
# print(list3)
# print(list3)
# str = "+".join(list3)
# print(str)
#
# print(("str"))
#print(list("str"))
#a = list("str")
res = isinstance("1",str)
a = list("111")
print(a)
b = tuple("111")
print(b)

state = "D"
if state.lower() in ["d","a"]:
    print(state)

def fun(str):
    return str.rstrip().split()

def floorList(li):
    li2 = []
    for item in li:
        li2.extend(item)
    return li2
file = open("input.txt","r")
ll = [fun(infile) for infile in file]
ll2 = floorList(ll)
print(ll)
print(ll2)

