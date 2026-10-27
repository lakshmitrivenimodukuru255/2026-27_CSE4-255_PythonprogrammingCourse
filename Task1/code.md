## Problem Statement:
   To design, develop, and document a programmatic solution for evaluating student scholarship applications. The system must process academic records, attendance metrics, and financial status against predetermined institutional thresholds to render a conclusive eligibility decision.
&nbsp;

## Algorithm
Start&nbsp;

Read student_name&nbsp;

Read numerical grades for five core subjects (python_marks, maths_marks, physics_marks, english_marks, c_programming_marks).&nbsp;

Read  attendance percentage (attendance) and annual family income (family_income).&nbsp;

Aggregate&nbsp;
total_marks = sum ({python_marks} + {maths_marks} + {physics_marks} + {english_marks} + {c_programming_marks})&nbsp;

marks_percentage= {total_marks}/{500} \times 100&nbsp;

Evaluate &nbsp;
{If } ({marks\_percentage} >= 60) { AND } ({attendance} >= 75) { AND } ({family\_income} >= 100000)

Branch A (True): Confirm applicant qualification for the scholarship.&nbsp;

Branch B (False): Reject applicant qualification due to unmet criteria.&nbsp;
  
Output results and terminate execution.&nbsp;
&nbsp;

## Python Source Code

student_name = input("Enter student name: ")&nbsp;
python_marks = float(input("Enter Python marks: "))&nbsp;
maths_marks = float(input("Enter Maths marks: "))&nbsp;

physics_marks = float(input("Enter Physics marks: "))&nbsp;
english_marks = float(input("Enter English marks: "))&nbsp;

c_programming_marks = float(input("Enter C Programming marks: "))&nbsp;

attendance = float(input("Enter attendance percentage (%): "))&nbsp;

family_income = float(input("Enter family income: "))&nbsp;

total_marks = (
    python_marks 
    + maths_marks 
    + physics_marks 
    + english_marks 
    + c_programming_marks
)&nbsp;

marks_percentage = (total_marks / 500) * 100&nbsp;


if marks_percentage >= 60 and attendance >= 75 and family_income < 100000:&nbsp;
    print(f"\nResult: {student_name} is eligible for the scholarship")
else:&nbsp;
    print(f"\nResult: {student_name} is not eligible for the scholarship")

&nbsp;
    
## Sample Test Cases
   
Case 1:
Sample Input &nbsp;

Enter student name: Rahul Verma&nbsp;

Enter Python marks: 75&nbsp;

Enter Maths marks: 80&nbsp;

Enter Physics marks: 70&nbsp;

Enter English marks: 85&nbsp;

Enter C Programming marks: 78&nbsp;

Enter attendance percentage (%): 85&nbsp;

Enter family income: 75000&nbsp;

Sample Output 
&nbsp;

Rahul Verma is eligible for the scholarship&nbsp;


Case 2:

Sample Input
&nbsp;

Enter student name: Priya Singh&nbsp;
Enter Python marks: 80&nbsp;
Enter Maths marks: 85&nbsp;
Enter Physics marks: 75&nbsp;
Enter English marks: 90&nbsp;
Enter C Programming marks: 82&nbsp;
Enter attendance percentage (%): 68&nbsp;
Enter family income: 60000&nbsp;

Sample Output
&nbsp;

Priya Singh is not eligible for the scholarship

 ## Flowchart

```mermaid
    A([Start]) --> B[Input student_name, subject marks, attendance, family_income]
    B --> C[Compute total_marks = Sum of 5 subject marks]
    C --> D[Compute marks_percentage = total_marks / 500 * 100]
    D --> E{marks_percentage >= 60 <br/> AND attendance >= 75 <br/> AND family_income < 100000?}
    E -- True --> F[Print: student_name is eligible for the scholarship]
    E -- False --> G[Print: student_name is not eligible for the scholarship]
    F --> H([Stop])
    G --> H
