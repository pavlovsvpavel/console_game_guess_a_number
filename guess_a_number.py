import random

computer_choice = random.randint(1, 100)

while True:
    user_input = int(input("Enter a number between 1 and 100: "))

    if user_input == computer_choice:
        break

    if user_input < computer_choice:
        print("Too low")
    elif user_input > computer_choice:
        print("Too high")

print()
print("Congratulations!\nYou guessed the number!")
