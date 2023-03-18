# ask for user input
number = int(input("Enter a number: "))

# check if the number is divisible by 2, 3, and not 8
if number % 2 == 0 and number % 3 == 0 and number % 8 != 0:
    print("Yes")
else:
    print("No")
