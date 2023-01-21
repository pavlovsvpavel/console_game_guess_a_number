import random
drawing = """
╔═╗┬ ┬┌─┐┌─┐┌─┐  ┌─┐  ┌┐┌┬ ┬┌┬┐┌┐ ┌─┐┬─┐
║ ╦│ │├┤ └─┐└─┐  ├─┤  ││││ ││││├┴┐├┤ ├┬┘
╚═╝└─┘└─┘└─┘└─┘  ┴ ┴  ┘└┘└─┘┴ ┴└─┘└─┘┴└─
"""
print("Welcome to the game", end="")
print(drawing)

computer_choice = random.randint(1, 100)
user_input = int(input("Enter a number between 1 and 100: "))

while user_input != computer_choice:

    if user_input > 100 or user_input < 1:
        print("Wrong input!")
    else:
        if user_input < computer_choice:
            print("Too low.")
        elif user_input > computer_choice:
            print("Too high.")

    user_input = int(input("Enter new number: "))

print()
print("Congratulations!\nYou guessed the number!")
