def main():
    NE =[('Maine',30840,1.329), ('Vermont',9217, .626), ('New Hampshire', 8953, 1.321), ('Massachusetts', 7800, 6.646),
         ('Connecticut', 4842, 3.59) ,("Rhode Island", 1044, 1.05) ]

    NE.sort(key=lambda ne:len(ne[0]))
    print("Sorted by population in descending order: ")
    for i in NE:
        print(i[0],end="  ")

main()