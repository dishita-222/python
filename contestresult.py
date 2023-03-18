# Take inputs from the user
num_questions = int(input("Enter the number of questions in the contest: "))
num_correct = int(input("Enter the number of correct answers given by contestant: "))

# Calculate the total marks earned
total_marks = num_correct * 5

# Calculate the percentage of total marks earned
percentage = (total_marks / (num_questions * 5)) * 100

# Calculate the final grade
if percentage >= 91:
    grade = "A"
elif percentage >= 81:
    grade = "B"
elif percentage >= 71:
    grade = "C"
elif percentage >= 61:
    grade = "D"
else:
    grade = "F"

# Display the information for the contestant
print(f"Total marks earned: {total_marks}")
print(f"Percentage of total marks earned: {percentage:.2f}%")
print(f"Final grade: {grade}")
