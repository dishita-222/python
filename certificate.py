# Prompt the user to enter whether they are part of the workshop, 
# how many classes they have attended, and how many assignments they have submitted
is_part_of_workshop = input("Are you part of the workshop? (y/n) ").lower() == "y"
num_classes_attended = int(input("How many classes have you attended? "))
num_assignments_submitted = int(input("How many assignments have you submitted? "))

# Check if the student meets the criteria for receiving a certificate
if is_part_of_workshop and num_classes_attended >= 3 and num_assignments_submitted >= 3:
    print("Congratulations, you are eligible to receive a certificate!")
else:
    print("Sorry, you are not eligible to receive a certificate.")
