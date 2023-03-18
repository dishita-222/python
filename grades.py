# Prompt the user for a letter grade
letter_grade = input("Enter a letter grade (A, B, C, D, or F): ")

# Check the letter grade and print the corresponding GPA
if letter_grade.upper() == "A":
    print("The corresponding GPA is 4.0.")
elif letter_grade.upper() == "B":
    print("The corresponding GPA is 3.0.")
elif letter_grade.upper() == "C":
    print("The corresponding GPA is 2.0.")
elif letter_grade.upper() == "D":
    print("The corresponding GPA is 1.0.")
elif letter_grade.upper() == "F":
    print("The corresponding GPA is 0.0.")
else:
    print("Invalid letter grade.")
