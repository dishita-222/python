# Prompt the user for their favorite color
favorite_color = input("What's your favorite color? ")

# Check the user's favorite color and print a message accordingly
if favorite_color.lower() == "red":
    print("Red is a bold color!")
elif favorite_color.lower() == "blue":
    print("Blue is a calm color!")
elif favorite_color.lower() == "green":
    print("Green is a refreshing color!")
else:
    print(f"{favorite_color} is a nice color!")
