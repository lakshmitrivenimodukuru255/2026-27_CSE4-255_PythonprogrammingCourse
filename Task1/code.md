1. Problem Statement:&nbsp;
   
   To design, develop, and document a programmatic solution for evaluating student scholarship applications. The system must process academic records, attendance metrics, and financial status against predetermined institutional thresholds to render a conclusive eligibility decision.

3. System Algorithm&nbsp;
   
Initialize Execution: Start the program workflow.
Data Ingestion:Read the applicant's identifier (student_name).
Read numerical grades for five core subjects (python_marks, maths_marks, physics_marks, english_marks, c_programming_marks).
Read quantitative metrics for attendance percentage (attendance) and annual family income (family_income).
Data Computation:Aggregate individual scores:$$\text{total\_marks} = \sum (\text{python\_marks} + \text{maths\_marks} + \text{physics\_marks} + \text{english\_marks} + \text{c\_programming\_marks})
$$Derive the aggregate percentage:$$\text{marks\_percentage} = \left(\frac{\text{total\_marks}}{500}\right) \times 100
$$Conditional Evaluation:Evaluate the logical expression:$$\text{If } (\text{marks\_percentage} \ge 60) \text{ AND } (\text{attendance} \ge 75) \text{ AND } (\text{family\_income} < 100000)
$$Branch A (True): Confirm applicant qualification for the scholarship.
  Branch B (False): Reject applicant qualification due to unmet criteria.
Workflow Termination: Output results and terminate execution.


5. Python Source Code&nbsp;
   
student_name = input("Enter student name: ")

python_marks = float(input("Enter Python marks: "))
maths_marks = float(input("Enter Maths marks: "))
physics_marks = float(input("Enter Physics marks: "))
english_marks = float(input("Enter English marks: "))
c_programming_marks = float(input("Enter C Programming marks: "))

attendance = float(input("Enter attendance percentage (%): "))
family_income = float(input("Enter family income: "))

total_marks = (
    python_marks 
    + maths_marks 
    + physics_marks 
    + english_marks 
    + c_programming_marks
)
marks_percentage = (total_marks / 500) * 100


if marks_percentage >= 60 and attendance >= 75 and family_income < 100000:
    print(f"\nResult: {student_name} is eligible for the scholarship")
else:
    print(f"\nResult: {student_name} is not eligible for the scholarship")

    
4. Sample Test Cases&nbsp;
   
Case 1:
Sample Input &nbsp;&nbsp;
Enter student name: Rahul Verma
Enter Python marks: 75
Enter Maths marks: 80
Enter Physics marks: 70
Enter English marks: 85
Enter C Programming marks: 78
Enter attendance percentage (%): 85
Enter family income: 75000

Sample Output &nbsp;&nbsp;
Rahul Verma is eligible for the scholarship


Case 2:

Sample Input &nbsp;&nbsp;
Enter student name: Priya Singh
Enter Python marks: 80
Enter Maths marks: 85
Enter Physics marks: 75
Enter English marks: 90
Enter C Programming marks: 82
Enter attendance percentage (%): 68
Enter family income: 60000

Sample Output&nbsp;&nbsp;
Priya Singh is not eligible for the scholarship

6. Flowchart&nbsp;&nbsp;

```
    A([Start]) --> B[Input student_name, subject marks, attendance, family_income]
    B --> C[Compute total_marks = Sum of 5 subject marks]
    C --> D[Compute marks_percentage = total_marks / 500 * 100]
    D --> E{marks_percentage >= 60 <br/> AND attendance >= 75 <br/> AND family_income < 100000?}
    E -- True --> F[Print: student_name is eligible for the scholarship]
    E -- False --> G[Print: student_name is not eligible for the scholarship]
    F --> H([Stop])
    G --> H
```
