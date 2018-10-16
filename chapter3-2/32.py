str = input("Enter word to translate: ")
list = list(str);
res = True;
arr = ['a','e','i','o','u'];
arr2 = ['v','o','w','e','l']

while res:
    if list[0] in arr2:
        list.append('w')
        list.append('a')
        list.append('y')
        res = False
    elif list[0] in arr:
        list.append('a')
        list.append('y')
        res = False;
    else :
        list.append(list[0])
        del list[0]

str = "".join(list)

print("The word in Pig Latin is "+str+".")
