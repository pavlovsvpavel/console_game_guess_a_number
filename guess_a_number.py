import random
game_name = """
╔═╗┬ ┬┌─┐┌─┐┌─┐  ┌─┐  ┌┐┌┬ ┬┌┬┐┌┐ ┌─┐┬─┐
║ ╦│ │├┤ └─┐└─┐  ├─┤  ││││ ││││├┴┐├┤ ├┬┘
╚═╝└─┘└─┘└─┘└─┘  ┴ ┴  ┘└┘└─┘┴ ┴└─┘└─┘┴└─
"""
congrats_message = """
 _____                             _         _       _   _                 _ 
/  __ \                           | |       | |     | | (_)               | |
| /  \/ ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___| |
| |    / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __| |
| \__/\ (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \_|
 \____/\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___(_)
                    __/ |                                                    
                   |___/                                                     
__   __                     _       _                                        
\ \ / /                    (_)     | |                                       
 \ V /___  _   _  __      ___ _ __ | |                                       
  \ // _ \| | | | \ \ /\ / / | '_ \| |                                       
  | | (_) | |_| |  \ V  V /| | | | |_|                                       
  \_/\___/ \__,_|   \_/\_/ |_|_| |_(_)                                                                                                                                                                                                                                    
"""
print(game_name)

computer_choice = random.randint(1, 100)
user_input = input("Enter a number between 1 and 100: \n")

while not user_input.isdigit():
    print("Wrong input! Try again.")

    user_input = input("Enter a number between 1 and 100: \n")

user_input = int(user_input)

while user_input != computer_choice:

    if user_input > 100 or user_input < 1:
        print("The number is out of range.")
    else:
        if user_input < computer_choice:
            print("Too low.")
        elif user_input > computer_choice:
            print("Too high.")

    user_input = int(input("Enter new number: \n"))

print(congrats_message)
