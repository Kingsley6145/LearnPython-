subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))
subject4 = float(input("Enter marks for subject 4: "))

if subject1 < 0 or subject1 > 100 or subject2 < 0 or subject2 > 100 or subject3 < 0 or subject3 > 100 or subject4 < 0 or subject4 > 100:
    print("Invalid marks entered.")
else:
    
    average = (subject1 + subject2 + subject3 + subject4) / 4

    if average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print("Average Score:", average)
    print("Grade:", grade)
