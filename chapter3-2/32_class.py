a = input("Eeter a word")
b = "aeiouAEIOU"

i = 0
while i < len(a):
    if a[i] in b:
        break
    else:
        i+=1

if i == 0:
    print(a+"way")
else:
    print(a[i:]+a[:i]+"ay")