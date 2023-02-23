marks = float(input("Enter your marks in Computer Science: "))

if marks > 90:
    print("Grade: A+")
elif marks >= 80 and marks < 90:
    print("Grade: A")
elif marks >= 70 and marks < 80:
    print("Grade: B+")
elif marks >= 60 and marks < 70:
    print("Grade: B")
elif marks >= 50 and marks < 60:
    print("Grade: C+")
elif marks >= 40 and marks < 50:
    print("Grade: C")
else:
    print("Grade: F")