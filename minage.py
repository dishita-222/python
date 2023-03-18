# Prompt the user for four ages
age1 = int(input("Enter age 1: "))
age2 = int(input("Enter age 2: "))
age3 = int(input("Enter age 3: "))
age4 = int(input("Enter age 4: "))

# Determine the youngest age
youngest_age = min(age1, age2, age3, age4)

# Print out the youngest age
print(f"The youngest age is {youngest_age}.")
