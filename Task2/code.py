Name = input("Enter your name: ")
Maths = int(input("Enter your Maths marks: "))      
Physics = int(input("Enter your Physics marks: "))
Chemistry = int(input("Enter your Chemistry marks: "))

if (Maths < 0 or Maths > 100) or (Physics < 0 or Physics > 100) or (Chemistry < 0 or Chemistry > 100):
    print("Error: Marks must be between 0 and 100!")
else:
    Pass_mark = 35
    Grace_math = 0
    Grace_physics = 0
    Grace_chemistry = 0

    if Maths < Pass_mark:
        Grace_math = Pass_mark - Maths

    if Physics < Pass_mark:
        Grace_physics = Pass_mark - Physics

    if Chemistry < Pass_mark:
        Grace_chemistry = Pass_mark - Chemistry

    final_math = Maths + Grace_math
    final_physics = Physics + Grace_physics
    final_chemistry = Chemistry + Grace_chemistry

    total_marks = final_math + final_physics + final_chemistry
    percentage = total_marks / 3  

    if final_math >= Pass_mark and final_physics >= Pass_mark and final_chemistry >= Pass_mark:
        status = "Pass"
    else:
        status = "Fail"

    if status == "Fail":
        classification = "Fail"
    elif percentage >= 75:
        classification = "Distinction"
    elif percentage >= 60:
        classification = "First Class"
    elif percentage >= 50:
        classification = "Second Class"
    else:
        classification = "Pass Class"

    print("Math Final:", final_math)
    print("Physics Final:", final_physics)
    print("Chemistry Final:", final_chemistry)
    print("Total Marks:", total_marks)
    print("Percentage:", percentage)
    print("Status:", status)
    print("Classification:", classification)
