gram = 1
year =0
while gram > 0.5:
    gram *= 0.99988
    year += 1

print("Carbon-14 has a half-life of {0:d} years.".format(year))