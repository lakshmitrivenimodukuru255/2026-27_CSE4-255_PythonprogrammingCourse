Student_name = input("Enter student name: ")

Python_marks = float(input("Enter Python marks: "))
Maths_marks = float(input("Enter Maths marks: "))
Physics_marks = float(input("Enter Physics marks: "))
English_marks = float(input("Enter English marks: "))
C_programming_marks = float(input("Enter C Programming marks: "))

Attendance = float(input("Enter attendance %: "))
Family_income = float(input("Enter family income: "))

Total_marks = (
    Python_marks
    + Maths_marks
    + Physics_marks
    + English_marks
    + C_programming_marks
)
Marks_percentage = Total_marks / 500 * 100

if Marks_percentage >= 60 and Attendance >= 75 and Family_income < 100000:
    print(Student_name, "is eligible for scholarship")
else:
    print(Student_name, "is not eligible for the scholarship")
