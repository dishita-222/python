# Define the rent calculator function
def calculate_rent(rent, utilities, internet,cook):
    total_cost = rent + utilities + internet + cook
    return total_cost

# Ask the user for the rent, utilities, and internet cost
rent = float(input("Enter the monthly rent: Rs."))
utilities = float(input("Enter the monthly utilities cost: Rs"))
internet = float(input("Enter the monthly internet cost: Rs."))
cook = float(input("Enter the monthly cook cost: Rs."))

# Call the calculate_rent function and print the total cost
total_cost = calculate_rent(rent, utilities, internet,cook)
print("The total monthly cost is: Rs.{:.2f}".format(total_cost))
