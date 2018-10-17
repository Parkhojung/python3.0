i = 2014
popc = 137000
popi = 126000
rc = 0.0051
ri = 0.0135

while popi <= popc:
    i+=1
    popc *= (1+rc)
    popi *= (1+ri)

print(str(i),"year",sep="")
