gpa = eval(input("Enter your gpa: "))
if gpa < 3.3:
    honors = "."
if gpa >= 3.3:
    honors = " cum laude."
if gpa >= 3.6:
    honors = " magna cum laude."
if gpa >= 3.9:
    honors = " summa cum laude."

print("You graduated"+ honors)