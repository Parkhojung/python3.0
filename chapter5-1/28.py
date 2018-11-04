names = ["Donald Shell", "Harlan Mills","Donald Knuth","Alan Kay"]
setLN =set()
for name in names:
    setLN.add(name.split()[-1])
print(setLN)

setLN2 = set(name.split()[-1] for name in names)
print(setLN2)