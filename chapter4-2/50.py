def main():
    grade1 = int(input("Enter grade on midterm: "))
    grade2 = int(input("Enter grade on final exam: "))
    grade3 =semesterGrade(grade1, grade2)
    print("Semester Grade:",grade3)

def semesterGrade(grade1, grade2):
    score = (grade1+2*grade2)/3
    if score >= 90:
        grade3 = 'A'
    elif score >=80:
        grade3 = 'B'
    elif score >=70:
        grade3 = 'C'
    elif score >=60:
        grade3 = 'D'
    else:
        grade3 = 'F'

    return grade3

main();