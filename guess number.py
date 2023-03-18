import random

# Generate a random number between 1 and 13
random_num = random.randint(1, 13)

# Prompt the user to enter their guess
user_guess = input("Is the number above, below, or equal to 7? ")

# Check if the user's guess is valid
valid_guesses = ["above", "below", "equal to"]
if user_guess not in valid_guesses:
    print("Invalid guess. Please enter 'above', 'below', or 'equal to'.")
else:
    # Check if the user's guess matches the random number
    if (user_guess == "above" and random_num > 7) or (user_guess == "below" and random_num < 7) or (user_guess == "equal to" and random_num == 7):
        print("You win!")
    else:
        print("Sorry, you lose. The number was", random_num)
