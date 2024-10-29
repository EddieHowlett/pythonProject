student_marks = float(input("Please enter your grade to get your result: "))
print("The grade you have achieved is: ")

if 90 <= student_marks <= 100:
    print("A")
elif 80 <= student_marks < 90:
    print("B")
elif 70 <= student_marks < 80:
    print("C")
elif 60 <= student_marks < 70:
    print("D")
elif 0 <= student_marks < 60:
    print("F")
