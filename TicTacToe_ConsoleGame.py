# Importing the required modules.

import random
# Random for making computer choice random.

import os
# OS for clearing the console after each try.

import time
# Time to use sleep() function to give time for the user to read the previous round result.

# Score to keep track of rounds user and computer wins.
score = [0, 0]

# Total three choices for user and computer to choose one.
choices = ["ROCK", "PAPER", "SCISSORS"]

# Running the program three times to simulate best of three.
for i in range(1, 4):
    print(f'Round {i} of 3')

    # Computer choice is assigned randomly
    computer_choice = choices[random.randint(0, 2)]

    # User choice from the input
    user_choice = choices[int(input("Enter 1 for ROCK,\nEnter 2 for PAPER,\nEnter 3 for SCISSORS : ")) - 1]

    # Clearing the console before giving results of the round (cls for windows and clear for linux based systems)
    try:
        os.system('cls')
    except:
        os.system('clear')

    # Printing the players choices.
    print(f'User Choice: {user_choice}\nComputer Choice: {computer_choice}')

    # Conditions to calculate the results of the round.
    if user_choice == computer_choice:
        print("This round is a tie.")
    elif user_choice == choices[0] and computer_choice == choices[1]:
        print("Computer wins this round.")
        score[1] += 1
    elif user_choice == choices[0] and computer_choice == choices[2]:
        print("User wins this round.")
        score[0] += 1
    elif user_choice == choices[1] and computer_choice == choices[0]:
        print("User wins this round.")
        score[0] += 1
    elif user_choice == choices[1] and computer_choice == choices[2]:
        print("Computer wins this round.")
        score[1] += 1
    elif user_choice == choices[2] and computer_choice == choices[0]:
        print("Computer wins this round.")
        score[1] += 1
    elif user_choice == choices[2] and computer_choice == choices[1]:
        print("User wins this round.")
        score[0] += 1

    # Printing the scores after every round.
    print()
    print(f'Current Score of Computer: {score[1]}\nCurrent Score of user: {score[0]}')
    print()
    time.sleep(2)

# Finally printing the result of the best of three rounds.
print()
if score[0] == score[1]:
    print("The best of three result is a tie")
elif score[0] < score[1]:
    print("Computer wins the best of three.")
else:
    print("User wins the best of three.")
