popul = 7000000000
year = 2011
while popul < 8000000000:
    popul += popul*0.011
    year += 1

print("World population will be 8billion in the year {0:d}.".format(year))